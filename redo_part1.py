import search_strategies as ss
import data

def test_china():
    print('bfs(北京,上海):',ss.bfs('北京','上海',city_connection))
    print('dfs(北京,上海):',ss.dfs('北京','上海',city_connection))
    print('bfs_distance(北京,上海):',ss.bfs_strategy('北京','上海',city_connection,ss.sort_by_distance,city_info))
    print('dfs_minimal_transfers(北京,上海):',ss.dfs_strategy('北京','上海',city_connection,ss.sort_by_transfers,city_info))
    return

city_info = ss.get_city_info(data.China_cities)
ss.draw_geos(city_info)
thereshold = 700
city_connection = ss.get_city_connection(thereshold,city_info)
ss.draw_connections(city_info,city_connection)

test_china()
