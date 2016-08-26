#-*- coding:utf-8 -*-
from flask import  Flask
from flask import  make_response #用于返回Response对象
from flask import redirect #用于重定向
from flask import abort



app=Flask(__name__)




@app.route('/')
def index():
    return '<h1>hello ,word!</h1>'

@app.route('/user')
def remind():
    return '<h1>please login</h1>'

@app.route('/user/<name>')
def userinfo(name):
    return '<h1>hello,%s</h1>' % name

@app.route('/client')
def client():
    return 'client'


# 以元组的形式,返回状态码 和 header
@app.route('/error')
def error():
        return 'can`t find page',404
     #   return 'can`t finc page',404,{'header':'this is a header'}

#返回esponse 对象
@app.route('/responseObject')
def responseObject():
    res=make_response('<h1> this is a response</h1>')
    res.set_cookie('answer', '42')
    return res

#重定向
@app.route('/redirect')
def redirected():
    return redirect('http://www.baidu.com')


@app.route('/abort/<count>')
def makeAAbort(count):
  #  if count==0:
        abort(404)
  #  else:
   #     return ' 还不错呀'

if __name__ == '__main__':
         app.run(debug=True)
