
from flask import Flask, render_template

myapp = Flask(__name__)



@myapp.route('/')
def homepage():


    return render_template('//template/prova_01.html')


@myapp.route('/prova')
def homepageProva():


    return "prova page di flask"





if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port=80)

