import flask, json
from flask import request

server = flask.Flask(__name__);

@server.route('/xxGet', methods = ['GET'])
def xxGet():
    fsf = request.values.get('fsf');
    jsf = request.values.get('jsf');
    xxlx = request.values.get('xxlx');
    messages = request.values.get('messages');
    if (jsf == '100003') and (fsf != '100001'):
        response = {'code':404,'message':'It is not from FY!'};
    if (jsf == '100003') and (fsf == '100005'):
        response = {'code':200,'message':'JCY got a message from GA'};
    return json.dumps(response, ensure_ascii=False);


def xxXml():
    xx = "";

def xxFile():
    filename = "e";
@server.route('/login', methods =  ['POST', 'GET'])
def login():
    username = request.values.get('name');
    password = request.values.get('password');
    if username and password:
        if (username=='admin') and  (password == 'admin'):
            response = {'code':200,'message':'login success'};
        else:
            response = {'code':203,'message':'wrong username or password'};
    else:
        response = {'code':418,'message':'username or password is null'}
    return json.dumps(response, ensure_ascii=False);
def run():
    server.run(debug=True, port=8080, host='0.0.0.0');