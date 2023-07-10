from flask import Flask, render_template
from routes.routeAdmin import admin_bp
from routes.routeMain import main_bp

myapp = Flask(__name__)

myapp.register_blueprint(main_bp, url_prefix = '/main')
myapp.register_blueprint(admin_bp, url_prefix = '/admin')


if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port = 80)




