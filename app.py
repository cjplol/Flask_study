#从flask包中导入Flask类
from flask import Flask,render_template

#使用Flask类创建一个app对象
#__name__：代表当前app.py模块
#1.以后出现bug，他可以帮助我们快速定位
#2.对于寻找模板文件，有一个相对路径
app=Flask(__name__)

class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
@app.route('/')
def show_index():
    person={
        "username":"cjp",
        "email":"xx@qq.com"
    }
    return render_template('index.html',person=person)

@app.route("/test_report/<report_id>")
def test_report(report_id):
    user=User(username="cjp666",email="xx@qq.com")
    return render_template("test_report.html",report_id=report_id,user=user)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=1234)