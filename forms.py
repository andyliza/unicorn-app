from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField



class AddForm(FlaskForm):
    name = StringField('Name of Unicorn:')
    submit = SubmitField('Add Unicorn')

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Unicorn to Remove:')
    submit = SubmitField('Remove Unicorn')

class DataBaseForm(FlaskForm):
    endpoint = IntegerField('Please key in the Database Endpoint: ')
    dbusername= IntegerField('Pleaase key in the Database Username: ')
    dbpassworkd= PasswordField('Please key in the Database Password: ')
