from flask import render_template, request, Blueprint
from webpersonal.models import Project
from flask_login import login_user, current_user, logout_user, login_required


core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/contact')
def contact():
    return render_template('contact.html')

@core.route('/portfolio')
def portfolio():
    projects = Project.query.all()
    return render_template('portfolio.html', projects=projects)