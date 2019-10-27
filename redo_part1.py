import re
import math
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import data




def get_city_info(coordination_data):
    # to get the city names and the corresponding city locations from the original data
    city_geos = {}
    for eachline in coordination_data.split("\n"):
        if eachline.startswith("//"): continue
        if eachline.strip() == "": continue # The strip() method returns a copy of the string with both leading and trailing characters removed

        city = re.findall("name:'(\w+)'",eachline)[0] # bracks represent that we only want the stuff int the brakets,onlyt take the first city,without [0] it will also show '[[兰州]]'
        city_geo = re.findall("geoCoord:\[(\d+.\d+),\s(\d+.\d+)\]",eachline)[0] #add '\'infront of the '[' and ']' because '[' and ']' has special meaning in RE, so we need to transfer '[' into only the symble '[' by making it into '\['
        city_geo = tuple(map(float,city_geo)) # 为什么要map成 tuple？后面的计算距离函数的input就是tuple。Returns a list of the results after applying the given function to each item of a given iterable
        # map()相当于给每个city_geo执行一个string变为float的过程，因为要用数值，后面还需要计算
        city_geos[city] = city_geo
    return city_geos

def geo_distance(origin, destination):
    #conpute the distance between cities using the location coordinates
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------

    origin = (48.1372, 11.5756)  # Munich
    destination = (52.5186, 13.4083)  # Berlin
    round(distance(origin, destination), 1) # 保留一位小数

    # roung() 第一个参数是一个浮点数; 第二个参数是保留的小数位数，可选，如果不写的话默认保留到整数
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

# to pack geo_distance in to a function to get the distance by inputting the city names:
def get_city_distance(city1,city2):
    return geo_distance(city_info[city1],city_info[city2])

# to get and draw the connection of the cities
def get_city_connection(thereshold):
    city_connection = defaultdict(list)

    for city_1 in list(city_info.keys()):
        for city_2 in list(city_info.keys()):
            if city_1 == city_2:
                continue
            if get_city_distance(city_1, city_2) < thereshold:
                city_connection[city_1].append(city_2)
    return city_connection

def draw_geos(city_info):
    # to display Chinese when networkx is used
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    graph = nx.Graph()  # to create a node
    graph.add_nodes_from(list(city_info.keys()))  # to add nodes in the graph
    # nx.draw(graph, city_info, with_labels=True) # big blue dots
    nx.draw(graph, city_info, with_labels=True, node_size=1)
    plt.show()
    return

def draw_connections(city_info,graph_info):
    # to display Chinese when networkx is used
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    graph = nx.Graph(graph_info)  # to create a node
    nx.draw(graph, city_info, with_labels=True, node_size=1)
    plt.show()
    return


def bfs(starter, destination, graph):
    pathes = [[starter]]
    visited = set()

    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]

        if frontier in visited: continue

        successor = graph[frontier]

        for node in successor:
            if node in path: continue

            new_path = path + [node]
            pathes.append(new_path)

            if node == destination:
                return new_path

        visited.add(frontier)


def dfs(starter, destination, graph):
    pathes = [[starter]]
    visited = set()

    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]

        if frontier in visited: continue

        successor = graph[frontier]

        for node in successor:
            if node in path: continue

            new_path = path + [node]
            pathes = [new_path] + pathes

            if node == destination:
                return new_path

        visited.add(frontier)


def bfs_strategy(starter, destination, graph, search_strategy):
    pathes = [[starter]]

    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]

        successor = graph[frontier]
        for node in successor:
            if node in path: continue
            new_path = path + [node]
            pathes.append(new_path)
        pathes = search_strategy(pathes)

        if pathes and pathes[0][-1] == destination:
            return pathes[0]


def dfs_strategy(starter, destination, graph, search_strategy):
    pathes = [[starter]]

    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]

        successor = graph[frontier]
        for node in successor:
            if node in path: continue
            new_path = path + [node]
            pathes = [new_path] + pathes
        pathes = search_strategy(pathes)

        if pathes and pathes[0][-1] == destination:
            return pathes[0]


def sort_by_distance(pathes):
    # search strategy according to the distance
    def get_path_distance(path):
        distance = 0
        for i, _ in enumerate(path[:-1]):  # list index out of range if without path[:-1]
            distance += get_city_distance(path[i], path[i + 1])
        return distance
    return sorted(pathes, key=get_path_distance)


def sort_by_transfers(pathes):
    # search strateg according to the minimal transfers
    def get_minimal_transfers(path):
        return len(path)
    return sorted(pathes, key = get_minimal_transfers)

def test():
    print('bfs(北京,上海):',bfs('北京','上海',city_connection))
    print('dfs(北京,上海):',dfs('北京','上海',city_connection))
    print('bfs_distance(北京,上海):',bfs_strategy('北京','上海',city_connection,sort_by_distance))
    print('dfs_minimal_transfers(北京,上海):',dfs_strategy('北京','上海',city_connection,sort_by_transfers))
    return

city_info = get_city_info(data.China_cities)
draw_geos(city_info)
thereshold = 700
city_connection = get_city_connection(thereshold)
draw_connections(city_info,city_connection)
test()

