# encoding UTF-8

import urllib.request
from bs4 import BeautifulSoup

from dbutil import save_stu_to_db, finish_save_stu_to_db
from parserHTML import get_students_info

list = get_students_info("0611401")

for stu in list:
    print(stu.toString())
    save_stu_to_db(stu)
finish_save_stu_to_db()
# url = "http://jwzx.cqupt.edu.cn/pubBjStu.php?bj=0111201"
# data = urllib.request.urlopen(url).read()
# data = data.decode('gbk')
# soup = BeautifulSoup(data, "html5lib")
# list_stus = soup.find_all(height='23')
# print(len(list_stus))
# for stu in list_stus:
#     stu = stu.find_all("td")
#     stu = Student(stu)
#     print(stu.toString())



##print(soup.prettify())
##list_stus = soup.table.find_all("tr")
##list_stus = soup.find_all(height='23')

##print(len(list_stus))
##list_stus = list_stus[1]
##print(len(list_stus))
















##for stu in list_stus:
##    print(stu)
##print(list_stus[1])
##for i,info in enumerate(list_stus[1].children):
##print(info)








# for stu in  list_stus:
# print(stu)
##for info in stu.descendants:
##print(info)
##print("这里的长度是list_stus："+len(list_stus).__str__())
##for stu in list_stus:
##person_info = stu.find_all("td")
##print("这里的长度是person_info："+len(person_info).__str__())




##for i, person in enumerate(person_info):
##  print(i.__str__() + person.string)
