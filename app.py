#从flask包中导入Flask类
from flask import Flask

#使用Flask类创建一个app对象
#__name__：代表当前app.py模块
#1.以后出现bug，他可以帮助我们快速定位
#2.对于寻找模板文件，有一个相对路径
app=Flask(__name__)

#创建一个路由和视图函数的映射
@app.route('/')
def hello_world():
    return 'Hello 中国！'

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
    app.run(debug=True,host='0.0.0.0',port=1234)