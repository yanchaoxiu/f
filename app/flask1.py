# # coding:utf-8
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return '''
#         <h1>My Home Page</h1>
#         <u1>
#             <li><a href="/music">Music</a></li>
#             <li><a href="/movie">Movie</a></li>
#             <li><a href="/book">Book</a></li>
#         </ul>
#     '''
# @app.route('/music')
# def music():
#     return '<h1>my favorite music</h1>'
# @app.route('/movie')
# def movie():
#     return '<h1>my favorite movie</h1>'
# @app.route('/book')
# def book():
#     return '<h1>my favorite book</h1>'
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#         <form action ="/auth" method="POST">
#             <input type ="text" name="uid">
#             <input type="password" name="pwd">
#             <input type ="submit" value="submit">
#         </form>
#     '''
# @app.route('/auth',methods=['POST'])
# def v_auth():
#     return '<h1>测试，测试<h1>'
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#         <h1>Users</h1>
#         <u1>
#             <li><a href="/user/Mary">Mary</a></li>
#             <li><a href="/user/linda">linda</a></li>
#             <li><a href="/user/SCH">SCH</a></li>
#         </u1>
#     '''
#
# @app.route('/user/<uname>')
# def v_user(uname):
#     return '<h1>%s\' ProFile<h1>' % uname
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask
# import os
# app = Flask(__name__)
# @app.route('/file/<path:fname>')
# def v_file(fname):
#     fullname = os.path.join('var/readonly/',fname)
#     f = open(fullname)
#     cnt = f.read()
#     f.close()
#     return cnt
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     return '<h1>home page</h1>'
#
# @app.route('/about')
# def v_about():
#     return '<h1>about me</h1>'
# print app.url_map
# print app.view_functions
# app.run(debug=True)


# #coding:utf-8
# def init_static_folder(app):
#     import os
#     try:
#         os.mkdir(os.path.join(app.root_path,'static'))
#         f=open(os.path.join(app.root_path,'static','1.txt'),'w')
#         f.write('this is a static file')
#         f.close()
#     except:
#         pass
#
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#         <h1>Home Page</h1>
#         <a href="/static/1.txt">1.txt</a>
#         '''
# init_static_folder(app)
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask,url_for
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print url_for('v_contacts')
#     return 'see console output'
# @app.route('/contact')
# def v_contacts():
#     pass
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask,url_for
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print url_for('v_contacts',format='json')
#     return '123'
# @app.route('/contact')
# def v_contacts():
#     pass
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask,url_for
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print url_for('v_contacts',name='julia',format='html')
#     return ''
# @app.route('/contact/<name>')
# def v_contacts(name):
#     pass
# app.run(debug=True)

# #coding:utf-8
# from flask import Flask,url_for
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print url_for('v_contacts',_anchor='part2')
# @app.route('/contact')
# def v_contacts():
#     pass
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask,url_for
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print url_for('v_contacts',_external='True')
# @app.route('/contact')
# def v_contacts():
#     pass
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask,url_for
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print url_for('v_contacts')
#     print url_for('v_contacts',name='yan')
#     print url_for('v_contacts',name='yan',ret='json')
#     print url_for('v_contacts',name='yan',_external=True)
#     print url_for('v_contacts',name='yan',_external=True,_scheme='https')
#     print url_for('v_contacts',name='yan',_anchor='photo')
#     return 'see console output'
# @app.route('/contact',methods=['POST','GET'])
# def v_contacts():
#     pass
# app.run(debug=True)




# #coding:utf-8
# from flask import Flask,request
# import os
# import urllib
#
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print request.headers
#     return 'see console output'
# app.run(debug=True)


# # coding:utf-8
# from flask import Flask,request,url_for
# app=Flask(__name__)
#
# @app.route('/')
# def v_index():
#     return '''
#     <form action ="/login" method="POST">
#         <input type ="text" name ="uid"
#         placeholder="input your user id">
#         <input type="password" name ="pwd"
#         placeholder="input your password">
#         <input type ="submit" name ="login">
#     </form>
#     '''
#
# @app.route('/login',methods=['POST'])
# def v_login():
#     uid= request.form['uid']
#     pwd=request.form['pwd']
#     if uid =='admin' and pwd=='111':
#         return 'authorized successfully'
#     else:
#         return 'un-authorized'
# app.run(debug=True)


# # coding:utf-8
# from flask import Flask,request,url_for
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#     <form method ="GET" action ="/search">
#         <input type ="text" placeholder="input keywords"
#         value="Python Flask" name="q">
#         <input type="submit" value="search">
#     </form>
#     '''
# @app.route('/search')
# def v_search():
#     if 'q'in request.args:
#         ret='<p>searching %s... </p>' % request.args['q']
#     else:
#         ret='what do you want to search?'
#     return ret
# app.run(debug=True)


# #coding:utf-8
# from flask import Flask,request
# app = Flask(__name__)
# @app.route('/')
# def v_index():
#     print request.json
#     return "see output console"
# app.run(debug=True)

# #coding:utf-8
# from flask import Flask,make_response
# app = Flask(__name__)
# @app.route('/ping')
# def v_ping():
#     rsp=make_response('pong')
#     rsp.mimetype='text/plain'
#     rsp.headers['x-tag']='sth.magic'
#     return rsp
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,make_response,url_for
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return '<a href="%s">ping</a>' % url_for('v_ping')
# @app.route('/ping')
# def v_ping():
#     return 'pong'
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,request,make_response,url_for
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     rsp=make_response('go <a href="%s">page2</a>' % url_for('v_page2'))
#     rsp.set_cookie('user','yanchaoxiu')
#     return rsp
# @app.route('/page2')
# def v_page2():
#     user=request.cookies['user']
#     return 'you are %s'% user
# app.run(debug=True)


# from flask import json
# a=[1,2,3]
# print json.dumps(a)
# b={'x':1,'y':2}
# print json.dumps(b)


# # coding:utf-8
# from flask import Flask,json
# app=Flask(__name__)
# users=['linda','marion','race']
# @app.route('/')
# def v_index():
#     return json.dumps(users),200,[('Content-Type','application/json;charset=utf-8')]
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,redirect
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return redirect('/newbies')
# @app.route('/newbies')
# def v_newbies():
#     return 'this page is for newbies only'
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,abort,request
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#         <ul>
#             <li><a href="admin?token=111">allowed</a></li>
#             <li><a href="/admin">forbidden</a></li>
#         </ul>
#     '''
# @app.route('/admin')
# def v_admin():
#     if 'token' in request.args:
#         return 'you are a good girl'
#     else:
#         abort(401)
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,session,request
# app=Flask(__name__)
# app.secret_key='yan123'
# @app.route('/')
# def v_index():
#     if 'counter' not in session:
#         session['counter']=0
#     session['counter']=session['counter']+1
#     return 'this is your %d times visit' % session['counter']
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,session,request
# from flask.globals import _request_ctx_stack,_app_ctx_stack
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     print request
#     print _request_ctx_stack.top.request
#     print _app_ctx_stack.top
#     return 'see console output'
# print _request_ctx_stack.top
# print _app_ctx_stack.top
# app.run(debug=True)


# # coding:utf-8
# from flask import Flask,session,url_for
# app=Flask(__name__)
# app.config['SERVER_NAME']='coupled.com'
# @app.route('/')
# def v_index():
#     return 'home page'
# @app.route('/genius')
# def v_genius():
#     return 'nothing special'
# with app.app_context():
#     print url_for('v_genius')

# # coding:utf-8
# from flask import Flask, session, url_for,request
# app = Flask(__name__)
# @app.route('/genius')
# def genius():pass
# print request

# from flask import Flask, session, url_for,request
# app = Flask(__name__)
# env={
#     'SERVER_NAME':'fake.com',
#     'SERVER_PORT':'80',
#     'REQUEST_METHOD':'GET',
#     'PATH_INFO':'/genius',
#     'wsgi.url_scheme':'http'
# }
# with app.request_context(env):
#     print request

# from flask import Flask, session, url_for,request
# app = Flask(__name__)
# with app.test_request_context('/genius',method='GET'):
#     print request

from flask import Flask, session, url_for,request
app = Flask(__name__)
@app.route('/genius')
def genius():
    return 'nothing special'
with app.test_request_context('/genius',method='GET'):
    print app.dispatch_request()

# # coding:utf-8
# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def index():
#     return 'this is not the point'
# @app.before_first_request
# def before_first_req():
#     print 'before process first request'
# @app.before_request
# def before_req():
#     print 'before process request'
# @app.after_request
# def after_req(rsq):
#     print 'after process request'
#     return rsq
# @app.teardown_request
# def teardown_reqctx(e):
#     print 'teardown process context'
# @app.teardown_appcontext
# def teardown_appctx(e):
#     print 'teardown application context'
# app.run(debug=True)

# # coding:utf-8
# from flask import render_template
# from app import app
# @app.route('/')
# @app.route('/index')
# def index():
#     user={'nickname':'Miguel'}
#     return render_template("index.html",title='Home',user=user)
# app.run(debug=True)