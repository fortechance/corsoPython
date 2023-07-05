from flask import Flask, render_template


myapp = Flask(__name__)

@myapp.route('/')
def homepage():

    return render_template('prova_01.html')



@myapp.route('/notizie')
def homepageProva():

    return render_template('ansa.html')

@myapp.route('/prova/<int:numero>')
def func01(numero):
    return 'hai scelto il numero' + str(numero)


if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port = 80)




