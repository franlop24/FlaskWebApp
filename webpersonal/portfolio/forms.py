from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, URL
from flask_wtf.file import FileField, FileAllowed

class CreateProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    web = StringField('Página Web', validators=[URL()])
    image = FileField('Imagen', validators=[DataRequired(),FileAllowed(['jpg','png'])])
    submit = SubmitField('Save')

class UpdateProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    web = StringField('Página Web', validators=[URL()])
    image = FileField('Imagen', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')