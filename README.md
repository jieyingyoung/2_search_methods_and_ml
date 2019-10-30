# 2_search_methods_and_ml

#### For practice:

##### -`data.py`

##### -`search_strategies.py`

##### -`redo_part1.py`

##### -`redo_part2.py`

##### -`RE_practice.py` 




#### For main:

##### -`get_subway_info.py` : 
to get the names of the Beijing subway stations and the coordinates of the stations.
##### Output: a json file named `subway_info.json`

##### -`search_strategies.py` : 
The first part shows the functions that are used in the lecture, and the second part shows 
the functions that are used in cleaning the data of Beijing Subways. Searching strategies are extended to four, from 
the lecture, which are, bfs, dfs, bfs with strategies and  dfs with strategies, where searching strategies include 
sorting according to the distance and sorting according to the minimal transfer. 

##### -`main.py` : 
This file runs the above functions using the data that are produced from `get_subway_info.py` and tests the results of 
them, and some notes are added.

##### -`北京地铁站生成坐标图.png` in folder `pics`

##### - `subway_info.json`  which is produced and stores the subway information that is grabbed from the Internet.




### The outputs of the main are: 

- bfs (通州北关站,白堆子站): ['通州北关站', '白石桥南站', '白堆子站'] 

- dfs (通州北关站,白堆子站): ['通州北关站', '花园桥站', '金台路站', '善各庄站', '枣营站', '北工大西门站', '将台站', '大望路站', '育知路站', '什刹海站', '霍營站', '上地站', '西直门站', '中关村站', '国家图书馆站', '白堆子站'] 

- bfs_minimal_transfers(通州北关站,白堆子站): ['通州北关站', '白石桥南站', '白堆子站'] 

- *Not be able to wait until it calculating the bfs_minimal_distance, the reason is writing below.



### Some notes (also answer the questions of optional analysis):

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
the transfer station that the station can reach. To have a better idea and manage it, I could learn from 
`https://github.com/lljieying/Subway_Data/blob/master/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81/bjsubwaySpider.py`
in which the author gives a unique number to each station in each subway line. 

4. In all, bfs with the minimal transfers algorithm shows the best results, as well as bfs shows. But there is still
a long way to go before reaching the Gaode map or Baidu map, in which more efficient and advanced algorithm is used as 
well as better ways to denote which is called 'connected'. That's what I'll improve. 
  

