from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from flask_app.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.route('/home')
def home():
    return render_template('home.html')

@bp.route('/search')
def search():
    return render_template('search.html')