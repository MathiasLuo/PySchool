from string import Template


def get_student(request, response_head):
    return "ccb" + request.path


def deftemplate(request, response_head):
    t = Template(file="template.html")
    t.title = "MathiasLuo's Title"
    t.contents = "MathiasLuo's contents"
    return str(t)
