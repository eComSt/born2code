from flask import Flask,send_from_directory,request

application = Flask(__name__)

@application.route("/")
def hello():
    return send_from_directory('/home/ecomstation/ttt/', 'index.html')

@application.route('/script.js')
@application.route('/style.css')
def static_root():
    return send_from_directory('/home/ecomstation/ttt/', request.path[1:])

if __name__ == "__main__":
    application.run()