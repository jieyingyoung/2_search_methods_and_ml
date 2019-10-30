import re
url = 'https://map.bjsubway.com/'
url2 = 'http://lbs.amap.com/console/show/picker'
# r = requests.get(url)
# print(r.content)
# # r.text

# html = ""
# while html == "":      #因为请求可能被北京地铁拒绝，采用循环+sleep的方式重复发送，但保持频率不太高
#     try:
#         page = requests.get(url, verify=False)
#         break
#     except:
#         print("Connection refused by the server..")
#         print("Let me sleep for 5 seconds")
#         print("ZZzzzz...")
#         sleep(5)
#         print("Was a nice sleep, now let me continue...")
#         continue
#
# # print(page.content)
#

names = ['草桥站','分离式岛式站', '巩华城站','菜市口站','岛式站','火车站','广阳城站','test_china' ]

names = [n.replace(r'(\w+)式站','') for n in names]
print(names)

# name = '岛式站'
# print(re.match(r'(\w+)式站',name))
def del_wrong_stations():
    for i,name in enumerate(names):
        if re.match(r'(\w+)式站', name) or any(x in name for x in ['巩华城站', '草桥站', '福寿岭站','高井站','广阳城站']):
            del names[i]
            del_wrong_stations()
            print(names)
    return names

print('name:',del_wrong_stations())
