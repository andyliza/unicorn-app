from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):
    name = StringField('Name of Unicorn:')
    submit = SubmitField('Add Unicorn')

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Unicorn to Remove:')
    submit = SubmitField('Remove Unicorn')
