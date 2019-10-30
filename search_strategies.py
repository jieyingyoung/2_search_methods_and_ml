import re
import math
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

'''
The first part shows the functions that used in the lecture, 
to get the data of the Chinese cities and the searching strategies.
 I extended the searching strategies to four: bfs, dfs, bfs with strategies 
 and  dfs with strategies, where searching strategies include sorting 
 according to the distance  and sorting according to the minimal transfer
 ------------------------------------------------------------
 '''

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
def get_city_distance(city1,city2,city_info):
    return geo_distance(city_info[city1],city_info[city2])

# to get and draw the connection of the cities
def get_city_connection(thereshold,city_info):
    city_connection = defaultdict(list)

    for city_1 in list(city_info.keys()):
        for city_2 in list(city_info.keys()):
            if city_1 == city_2:
                continue
            if get_city_distance(city_1, city_2,city_info) < thereshold:
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


def bfs_strategy(starter, destination, graph, search_strategy,city_info):
    pathes = [[starter]]

    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]

        successor = graph[frontier]
        for node in successor:
            if node in path: continue
            new_path = path + [node]
            pathes.append(new_path)
        pathes = search_strategy(pathes,city_info)

        if pathes and pathes[0][-1] == destination:
            return pathes[0]


def dfs_strategy(starter, destination, graph, search_strategy,city_info):
    pathes = [[starter]]

    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]

        successor = graph[frontier]
        for node in successor:
            if node in path: continue
            new_path = path + [node]
            pathes = [new_path] + pathes
        pathes = search_strategy(pathes,city_info)

        if pathes and pathes[0][-1] == destination:
            return pathes[0]


def sort_by_distance(pathes,city_info):
    # search strategy according to the distance
    def get_path_distance(path):
        distance = 0
        for i, _ in enumerate(path[:-1]):  # list index out of range if without path[:-1]
            distance += get_city_distance(path[i], path[i + 1],city_info)
        return distance
    return sorted(pathes, key=get_path_distance)


def sort_by_transfers(pathes,city_info):
    # search strateg according to the minimal transfers
    def get_minimal_transfers(path):
        return len(path)
    return sorted(pathes, key = get_minimal_transfers)

'''
the second part shows the functions that used in splitting the data of Beijing Subways 
------------------------------------------------------------
'''

# the following two functions are to split data and line from the original dataset
def get_station_info(data):
    """
    This function is to get the coordinates of the stations.
    :param data: A dictionary where keys are the names of the stations and values are either the coordinates or the line name.
    :return: a dictionary where only contains the station name as the key and the coordinates as the value.
    """
    station_info= {}
    for i,(station, location) in enumerate(zip(list(data.keys()), list(data.values()))):
        if i % 2 == 0:
            location = tuple(map(float, location))
            station_info[station] = location
    return station_info

def get_line_info(data):
    """
    This function is to get which line(lines if it is a connection station) a station belongs to.
    :param data: A dictionary where keys are the names of the stations and values are either the coordinates or the line name.
    :return: a dictionary where only contains the station name as the key and the line name as the value.
    """
    line_info= {}
    for i,(station, line) in enumerate(zip(list(data.keys()), list(data.values()))):
        if i % 2 != 0:
            station = station[0:-2]
            line_info[station] = line
    return line_info

def get_station_distance(station1,station2,station_info):
    return geo_distance(tuple(map(float,station_info[station1])),tuple(map(float,station_info[station2])))


def get_station_connection(line_info,station_info, thereshold):
    '''
    This function is to get the connection of the stations.
    Rules: if two stations are in the same line, then they are connected; if a station is the transfer station of two lines, then the station is connected
    with all the stations of the two lines.
    :param line_info: A dictionary where names are the station name and the values are which subway line they belong to
    :param station_info: A dictionary where names are the station name and the values are the coordinates
    :param thereshold: not necessory, only use when calculate the connection according to the distance of the stations
    :return:
    '''
    station_connection = defaultdict(list)
    for station1,line1 in zip(list(line_info.keys()), list(line_info.values())):
        print(station1,line1)
        for station2, line2 in zip(list(line_info.keys()), list(line_info.values())):
            print(station2,line2)
            if line1 == line2 or line2 in line1 or line1 in line2:
            # if get_station_distance(station1, station2, station_info) < thereshold:
                station_connection[station1].append(station2)
            else: continue
    return station_connection

def draw_stations(station_info):
    '''
    This function draws the stations of beijing subway according to the coordinates
    :param station_info: dictionary where the keys are the station names and the values are the coordinates
    :return: a picture of the stations
    '''

    plt.rcParams['font.sans-serif'] = ['SimHei']# to display Chinese when networkx is used
    plt.rcParams['axes.unicode_minus'] = False

    graph = nx.Graph()  # to create a node
    graph.add_nodes_from(list(station_info.keys()))  # to add nodes in the graph
    # nx.draw(graph, station_info, with_labels=True) # big blue dots
    plt.figure(1, figsize=(40, 30))
    nx.draw(graph, station_info, with_labels=True, node_size=2,fontsize=20)
    font = {'color': 'r',
            'fontweight': 'bold',
            'fontsize': 30}
    # plt.title("北京地铁站坐标图", font)
    plt.show()
    return







