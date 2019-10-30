import json
import search_strategies as ss

with open ('subway_info.json') as js:
    data = json.load(js)
    print(data)

station1 = '通州北关站'
station2 = '白堆子站'

station_info = ss.get_station_info(data)
line_info = ss.get_line_info(data)
# print(line_info)

distance = ss.get_station_distance(station1,station2,station_info)
print('{} 到 {} 的距离是 : {} km'.format(station1,station2,round(distance,2)))

thereshould = 3
station_connection = ss.get_station_connection(line_info,station_info,thereshould)
print(station_connection)

ss.draw_stations(station_info)

def test_beijing():
    print('bfs ({},{}):{} '.format(station1,station2, ss.bfs(station1,station2,station_connection)))
    print('dfs ({},{}):{} '.format(station1, station2, ss.dfs(station1, station2, station_connection)))
    print('bfs_minimal_transfers({},{}):{} '.format(station1,station2,
                                                   ss.bfs_strategy(station1,station2,station_connection,ss.sort_by_transfers,station_info)))
    print('bfs_minimal_distance({},{}):{} '.format(station1, station2,
                                                   ss.bfs_strategy(station1, station2, station_connection,ss.sort_by_distance, station_info)))
    print('dfs_minimal_transfers({},{}):{} '.format(station1, station2,
                                                   ss.dfs_strategy(station1, station2, station_connection,ss.sort_by_transfers, station_info)))
    print('dfs_minimal_distance({},{}):{} '.format(station1, station2,
                                                   ss.dfs_strategy(station1, station2, station_connection,ss.sort_by_distance, station_info)))
    return

test_beijing()

'''
output:

bfs (通州北关站,白堆子站):['通州北关站', '白石桥南站', '白堆子站'] 

dfs (通州北关站,白堆子站):['通州北关站', '花园桥站', '金台路站', '善各庄站', '枣营站', '北工大西门站', '将台站', '大望路站', '育知路站', '什刹海站', '霍營站', '上地站', '西直门站', '中关村站', '国家图书馆站', '白堆子站'] 

bfs_minimal_transfers(通州北关站,白堆子站):['通州北关站', '白石桥南站', '白堆子站'] 

* Not be able to wait until it calculating the bfs_minimal_distance, reason is writing below.
'''

'''
Some notes (also answer the questions of optional assignment/analysis):
1. It's very slow to return the path according to the smallest distance, because: 
in the function `sort_by_transfers()` in `search_strategies.py`, it calculates the 
distance of a path by iterating each pair of stations and accumulate the whole distance
by adding them. To calculate each path, it takes O(n) time, and bfs and dfs both take O(b**d) time
for the worst case. After writing this, I stopped my computer which is running the algorithm of
the bfs_according_to_the_minimal_distance...


2. As what our lecturer said, bfs sometimes get the optimal results while dfs never, from the output 
above we can clearly see that. Luckily, we got the transfer at '白石桥南站' from ['通州北关站'to '白堆子站'],
which is also optimal in reality. But not all outputs are like this. 


3. Because in the `station_connection()` function in `search_strageties.py`,I connected the stations as 
following rules:
if two stations are in the same line, then they are connected; 
if a station is the transfer station of two lines, then the station is connected with all the stations of the two lines.
This leads a problem that if a subway line is very long, then the stations at both ends are connected.
In the searching result, it may lead us from '通州北关' (the most east end) to ’苹果园' (the most west end)
and then come back to ‘天安门西'(the middle part). To solve this problem, I could only connect the stations
with their neighbor stations (for example, only to connect '天安门西' with '天安门东' and ’西单' stations) as well as
the transfer station that the station can reach. But because of the limitation of time, I did not manage to 
finish this.

4. In all, bfs with the minimal transfers algorithm shows the best results, as well as bfs shows. But there is still
a long way to go before reaching the Gaode map or Baidu map, in which more efficient and advanced algorithm is used as 
well as better ways to denote which is called 'connected'. That's what I'll improve. 
  
'''