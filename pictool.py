import urllib.request
import os


sourceURL = r'http://jwzx.cqupt.edu.cn/showstuPic.php?xh='
save_path = r'\picture/'


def downpic(student):
    imgURL = sourceURL + student.stuId
    fileName = student.sex + "--" + student.name + "--" + student.major + "--" + student.college
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = urllib.request.urlopen(imgURL).read()


