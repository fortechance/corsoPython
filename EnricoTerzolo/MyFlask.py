from flask import Flask, request

from routes.routeAdmin import admin_bp
from routes.routeMain import main_bp

from loginAttivi import LoginAttivi

myapp = Flask(__name__)

myapp.register_blueprint(main_bp)


if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port = 80)




