import sqlite3

from stu import Student

CREART_TABLE = "CREATE TABLE STU (ID INTEGER  AUTO_INCREMENT PRIMARY KEY,NAME CHAR(100),STUID CHAR(50),MAJOR CHAR(50),SEX CHAR(50),COLLEGE CHAR(50));"

conn = sqlite3.connect("students.db")


# cursor = conn.cursor()
# cursor.execute(CREART_TABLE)
# cursor.close()
# conn.commit()
# conn.close()

def finish_save_stu_to_db():
    conn.commit()
    conn.close()
    print("保存成功了")


def get_sql_string(Student):
    return "INSERT INTO STU(NAME,STUID,MAJOR,SEX,COLLEGE) VALUES ('%s','%s','%s','%s','%s');" % (
    Student.name, Student.stuId, Student.major, Student.sex, Student.college);


def save_stu_to_db(student):
    cursor = conn.cursor()
    # print(get_sql_string(student))
    cursor.execute(get_sql_string(student))
    cursor.close()
