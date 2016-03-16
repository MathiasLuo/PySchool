from flask import Flask, request

from dbutil import query_stu_name

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return '<h1>Home</h1>'


@app.route("/getallstudents", methods=["GET", "POST"])
def getallStudent():
    return query_stu_name()


@app.route("/getstuinfo/<string:id>", methods=["GET"])
def getStudent(id):
    return query_stu_name(id)

if __name__ == "__main__":
    app.run()
