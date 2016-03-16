import sqlite3

CREART_TABLE = "CREATE TABLE STU (ID INTEGER  AUTO_INCREMENT PRIMARY KEY,NAME CHAR(100),STUID CHAR(50),MAJOR CHAR(150),SEX CHAR(50),COLLEGE CHAR(50));"

conn = sqlite3.connect("students.db")

# cursor = conn.cursor()
# cursor.execute(CREART_TABLE)
# cursor.close()
# conn.commit()
# conn.close()

def info():
    print("添加函数--->>>insert_stu(name,stuId,major,sex,college)")
    print("查找函数--->>>insert_stu(name)----query_stu_id(id)")
    print("更新函数--->>>update_stu_name(name,stuid)----update_stu_major(major,stuid)")
    print("删除函数--->>>delete_stu_id(stuid)----delete_stu_name(name)")
    print("提交函数--->>>save_to_db()")


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


def insert_stu(name, stuId, major, sex, college):
    sql_insert = "INSERT INTO STU(NAME,STUID,MAJOR,SEX,COLLEGE) VALUES ('%s','%s','%s','%s','%s');" % (
        name, stuId, major, sex, college)
    conn.execute(sql_insert)
    print("已经插入到数据库了")


def query_stu_name(name):
    sql_query = "SELECT * FROM STU WHERE NAME = ?"
    cursor = conn.execute(sql_query, [name])
    students = cursor.fetchall()
    for stu in students:
        print(stu)


def query_stu_id(stuid):
    sql_query = "SELECT * FROM STU WHERE STUID = ?"
    cursor = conn.execute(sql_query, [stuid])
    students = cursor.fetchall()
    for stu in students:
        print(stu)


def update_stu_name(name, stuId):
    sql_update = "UPDATE STU SET NAME='" + name + "'WHERE  STUID ='" + stuId + "'"
    conn.execute(sql_update)


def update_stu_major(major, stuId):
    sql_update = "UPDATE STU SET MAJOR='" + major + "'WHERE  STUID ='" + stuId + "'"
    conn.execute(sql_update)


def delete_stu_id(stuid):
    sql_delete = "DELETE FROM STU WHERE STUID ='" + stuid + "'"
    conn.execute(sql_delete)


def delete_stu_name(name):
    sql_delete = "DELETE FROM STU WHERE NAME = '" + name + "'"
    conn.execute(sql_delete)


def save_to_db():
    conn.commit()
    conn.close()


info()
