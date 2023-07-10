from flask import Blueprint, render_template

admin_bp = Blueprint('admin',__name__)

@admin_bp.route('/login')
def login():
    return 'Pagina di login'

@admin_bp.route('/dashboard', methods = ['GET'])
def dash():
    return 'Pagina Dashboard'