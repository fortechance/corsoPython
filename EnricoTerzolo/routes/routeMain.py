from flask import Blueprint, render_template

main_bp = Blueprint('main',__name__)

@main_bp.route('/')
def Index():
    return 'Pagina di index'

@main_bp.route('/prova1')
def prova1():
    return render_template('prova_01.html')
