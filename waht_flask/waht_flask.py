from flask import Flask
# app = Flask(__name__, static_url_path='/data_day')
app = Flask(__name__, static_url_path='')
# @app.route('/',methods = ['GET','POST'])
@app.route('/')
def index():
    # if flask.request.method == 'GET':
    #   return 'get'
    return app.send_static_file('index2.html')
    # return "post"
if __name__ == '__main__':
    app.run(host='192.168.1.233', port='8090',)
