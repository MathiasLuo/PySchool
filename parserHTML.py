import urllib

from bs4 import BeautifulSoup

from stu import Student


def get_students_info(class_number):
    stu_list = []
    data = urllib.request.urlopen(class_number).read()
    try:
        data = data.decode('gbk')
    except ValueError as e:
        pass
    soup = BeautifulSoup(data, "html5lib")
    list_stu = soup.find_all(height='23')
    for i,stu in enumerate(list_stu):
        if(i != 0):
            stu = stu.find_all("td")
            stu = Student(stu)
            # print(stu.toString())
            stu_list.append(stu)
    return stu_list


