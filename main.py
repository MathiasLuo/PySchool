from dbutil import save_stu_to_db, finish_save_stu_to_db
from parserHTML import get_students_info
from pictool import downpic
from reptile import get_urls, get_class_number

PATH = "http://jwzx.cqupt.edu.cn/pubBjStu.php"

urls = get_urls(PATH)

for tt in urls:
    list = get_class_number(tt)
    for i in list:
        stus = get_students_info(i)
        for stu in stus:
            print(stu.toString())
            save_stu_to_db(stu)


finish_save_stu_to_db()