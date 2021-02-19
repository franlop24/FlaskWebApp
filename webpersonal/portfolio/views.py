from flask import render_template, url_for, flash, request, redirect, Blueprint
from webpersonal.portfolio.forms import CreateProjectForm, UpdateProjectForm
from webpersonal.portfolio.image_handler import add_image
from webpersonal.models import Project
from webpersonal import db
from flask_login import login_user, current_user, logout_user, login_required

portfolio = Blueprint('portfolio', __name__, template_folder='templates/portfolio')

#create
@portfolio.route('/add', methods=['GET','POST'])
@login_required
def add_project():

    form = CreateProjectForm()

    if form.validate_on_submit():
        imagen = add_image(form.image.data)
        new_project = Project(title=form.title.data, description=form.description.data,image=imagen, web=form.web.data)

        db.session.add(new_project)
        db.session.commit()
        flash('Project Created!')
        return redirect(url_for('portfolio.list_project'))

    return render_template('create_project.html', form=form)

#View
@portfolio.route('/<int:project_id>')
@login_required
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', project=project)

#update
@portfolio.route('/<int:project_id>/update', methods=['GET','POST'])
@login_required
def update(project_id):

    project = Project.query.get_or_404(project_id)

    form = UpdateProjectForm()
    imagen_actual = project.image

    if form.validate_on_submit():
        project.title = form.title.data
        project.description = form.description.data
        if form.image.data is not None:
            imagen = add_image(form.image.data)
            project.image = imagen
        project.web = form.web.data
        db.session.commit()
        flash('Project Updated!')
        return redirect(url_for('portfolio.list_project'))

    elif request.method == 'GET':
        form.title.data = project.title
        form.description.data = project.description
        form.web.data = project.web
        imagen_actual = project.image
        #return render_template('create_project.html', form=form)

    return render_template('create_project.html', form=form, imagen=imagen_actual)

@portfolio.route('/')
@login_required
def list_project():
    projects = Project.query.all()
    return render_template('list_project.html', projects=projects)

@portfolio.route('/<int:project_id>/delete', methods=['GET','POST'])
def delete_project(project_id):

    project = Project.query.get_or_404(project_id)

    db.session.delete(project)
    db.session.commit()
    flash('Project Deleted!')
    return redirect(url_for('portfolio.list_project'))