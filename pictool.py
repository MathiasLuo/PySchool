import os
import urllib.request

sourceURL = r'http://jwzx.cqupt.edu.cn/showstuPic.php?xh='
save_path = r'picture/'


def downpic(student):
    print(student.stuId)
    path = student.stuId
    path = path.strip()
    imgpath = sourceURL + path
    filename = save_path+student.sex.strip()+ "--"+student.stuId.strip()+"--"+ student.name.strip() + "--" + student.major.strip() + "--" + student.college.strip()+".jpg"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = urllib.request.urlopen(imgpath).read()
    output = open(filename, "wb+")
    output.write(data)
    output.close()


