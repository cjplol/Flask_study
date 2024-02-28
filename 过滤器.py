#从flask包中导入Flask类
from flask import Flask,render_template
from datetime import datetime
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
    user=User(username="cjpnbnb",email="xx@qq.com")
    return render_template("filter.html",report_id=report_id,user=user)

'''
过滤器本质上是python函数，他会把被过滤的值当做第一个参数传给这个函数，函数经过一些逻辑处理后，再返回新的值。
在过滤器函数写好后，可以通过@app.template_filter装饰器或是app.add_template_filter函数来把函数注册成Jinja2能用的过滤器。
这里我们以注册一个时间格式化的过滤器为例，来说明下自定义过滤器的方法
'''
def datetime_format(value,format="%Y年%m月%d日%H:%M:%S"):
    return value.strftime(format)
app.add_template_filter(datetime_format,"dformat")

@app.route("/filter")
def filter_demo():
    user=User(username="cjp",email="xxx@qq.com")
    mytime=datetime.now()
    return render_template("filter.html",user=user,mytime=mytime)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=1234)