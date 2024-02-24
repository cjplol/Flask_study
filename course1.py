# 从flask包中导入Flask类
from flask import Flask, request

# 使用Flask类创建一个app对象
# __name__：代表当前app.py模块
# 1.以后出现bug，他可以帮助我们快速定位
# 2.对于寻找模板文件，有一个相对路径
app = Flask(__name__)

# 创建一个路由和视图函数的映射

'''
url:http[80]//https[443]://www.qq.com:443/path
url与视图：path与视图
'''


@app.route('/')
def hello_world():
    return 'Hello 中国！'


@app.route("/profile")
def profile():
    return "我是个人中心！"


@app.route("/blog/list")
def blog_list():
    return "我是博客列表！"


# 带参数的url:<int:blog_id> blog_id必须为整型
@app.route("/blog/<int:blog_id>")
def blog_detail(blog_id):
    return "您访问的博客是：{}".format(blog_id)


'''
/book/list:会给我返回第一页的数据
/book/list?page=2:获取第二页数据
'''


@app.route('/book/list')
def book_list():
    # 查询字符串方式传参
    # arguments:参数
    # request.args:类字典类型
    page = request.args.get("page", default=1, type=int)
    return f"您获取的是第{page}页的图书列表！"


'''
1.debug模式：代码改动不需要重新运行代码就可以显示
    app.run(debug=True)
    改动后ctrl+s，浏览器刷新

2.修改host：
    让其他电脑能访问到我电脑上的flask项目
    app.host(host='0.0.0.0')

3.修改端口号
    app.host(port=1234)
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234)