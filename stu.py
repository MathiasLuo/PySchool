class Student:
    def __init__(self, name, stuId, sex, major, college):
        self.name = name
        self.stuId = stuId
        self.sex = sex
        self.major = major
        self.college = college

    def toString(self):
        return "姓名：" + self.name \
               + "\n学号：" + self.stuId + "\n性别：" + self.sex + "\n专业：" + self.major + "\n学院：" + self.college

    def __init__(self, info):
        self.stuId = info[0].string.strip()
        self.name = info[1].string.strip()
        self.sex = info[2].string.strip()
        self.major = info[3].string.strip()
        self.college = info[4].string.strip()
