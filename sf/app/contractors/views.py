from flask import Blueprint, render_template, request

contractors = Blueprint('contractors', __name__)

@contractors.route('/')
def index():
    return render_template('index.html')

@contractors.route('/about')
def about():
    return 'about'
    