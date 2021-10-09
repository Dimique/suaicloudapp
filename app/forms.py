from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddStudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    group = StringField('Group', validators=[DataRequired()])
    submit = SubmitField('Submit')
