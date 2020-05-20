import flask, json
from flask import request

server = flask.Flask(__name__);

# @server.route() 将普通函数转变为服务
@server.route('/login', methods = ['get', 'post'])

def login():
    username = request.values.get('name');
    password = request.values.get('password');
    if username and password:
        if (username=='admin') and  (password == 'admin'):
            response = {'code':200,'message':'login success'};
            return json.dumps(response, ensure_ascii=False);
        else:
            response = {'code':203,'message':'wrong username or password'};
            return json.dumps(response, ensure_ascii=False);
    else:
        response = {'code':418,'message':'username or password is null'}
def mockrun():
    server.run(debug=True, port=8080, host='0.0.0.0');
    return json.dumps(response, ensure_ascii=False);