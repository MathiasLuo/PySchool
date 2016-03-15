import urllib

import re
from bs4 import BeautifulSoup

PATH = "http://jwzx.cqupt.edu.cn/pubBjStu.php"
BASE_PATH = "http://jwzx.cqupt.edu.cn/"


# data = urllib.request.urlopen(PATH).read()
# data = data.decode('gbk')
# soup = BeautifulSoup(data, "html5lib")
# urls = soup.find_all(language='javascript')
# data = urls[1].string
# ##print(data)
# data = data[25:6700 - 28]
# # print(data)
#
# data = data.split(r',')
# print(len(data))
# for tt in data:
#     if re.match(r'\'pubBjStu.php\?zyh=\d\d\d\d\'', tt):
#         print(tt)
# data = data.split("[\;]+")
# print(len(data))
# for tt in data[0].split("[\s\,\;]+"):
#     print(tt)
#     if re.match(r'\'pubBjStu.php\?zyh=\d\d\d\d\'', tt):
#         print(tt)

# CLASS_PATH="http://jwzx.cqupt.edu.cn/pubBjStu.php?zyh=5102"
# data = urllib.request.urlopen(CLASS_PATH).read()
# data = data.decode('gbk')
# soup = BeautifulSoup(data, "html5lib")
# data =soup.find_all("a")
# for tt in  data:
#     print(tt.get("href"))


def get_urls(url):
    list_urls = []
    data = urllib.request.urlopen(PATH).read()
    data = data.decode('gbk')
    soup = BeautifulSoup(data, "html5lib")
    urls = soup.find_all(language='javascript')
    data = urls[1].string
    data = data[25:6700 - 28]
    data = data.split(r',')
    for tt in data:
        if re.match(r'\'pubBjStu.php\?zyh=\d\d\d\d\'', tt):
            list_urls.append(BASE_PATH + tt[1:22])
    return list_urls


def get_class_number(url):
    urls = []
    data = urllib.request.urlopen(url).read()
    data = data.decode('gbk')
    soup = BeautifulSoup(data, "html5lib")
    data = soup.find_all("a")
    for tt in data:
        urls.append(BASE_PATH + tt.get("href"))
    return urls
