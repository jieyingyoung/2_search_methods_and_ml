from bs4 import BeautifulSoup
import requests
import re
import json

def get_location_from_amap(name, key, city ='北京市'): #
    # 通过高德开放平台获得地铁站location
    # https://lbs.amap.com/api/webservice/guide/api/search#text
    parameters = {'keywords': name, 'key': key, 'city': city, 'types': 150500}
    base = 'https://restapi.amap.com/v3/place/text?parameters'
    response = requests.get(base, parameters)
    answer = response.json()
    location = str(answer['pois'][0]['location']).split(',')
    line_name = str(answer['pois'][0]['address'])
    return location,line_name

# print(get_location_from_amap('通州北关','f08ea0494c3c4e98a8d72eebefadc8cf'))

def get_subway_names(): # 通过wiki 获得地铁站名 ,需要科学上网
    print('获取地铁站名字中...')
    url = 'https://zh.wikipedia.org/wiki/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E8%BD%A6%E7%AB%99%E5%88%97%E8%A1%A8'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser',from_encoding= 'utf-8')
    # print(soup)
    names_and_platforms = set(re.findall(r'title="(\w+)">', str(soup)))
    names = re.findall(r'(\w+站)',str(names_and_platforms))
    # to remove the miss-filtered stations:
    def del_wrong_stations():
        for i, name in enumerate(names): # the locations of these five stations cannot be retrived from 高德  amap
            if re.match(r'(\w+)式站', name) or any(x in name for x in ['巩华城站', '草桥站', '福寿岭站', '高井站', '广阳城站']):
                del names[i]
                del_wrong_stations()
                # print(names)
        return names
    names = del_wrong_stations()
    print(names)
    # print(len(names))
    print('获取地铁站名字已完成！')
    return names


subway_info = {}
# for name in ['通州北苑站']:
for name in get_subway_names():
    # print(name)
    print('获取地铁站坐标中...有点慢，请耐心等待...')
    subway_info[name] = get_location_from_amap(name,'f08ea0494c3c4e98a8d72eebefadc8cf')[0] # private key
    subway_info[name + '属于'] = get_location_from_amap(name,'f08ea0494c3c4e98a8d72eebefadc8cf')[1] # private key

print('获取地铁站坐标已完成！')
print(subway_info)

with open ('subway_info.json', 'w') as sb:
    json.dump(subway_info, sb)

print('北京地铁坐标信息已存储为subway_info.json文件！请查收！')

