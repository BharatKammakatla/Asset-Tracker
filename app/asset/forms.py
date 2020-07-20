from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class EditAssetForm(FlaskForm):
    type = StringField('Type', render_kw={'readonly': True})
    asset_name = StringField('Asset Name', render_kw={'readonly': True})
    person_name = StringField('Person', render_kw={'readonly': True})
    start_time = DateField('Start Time', render_kw={'readonly': True})
    end_time = DateField('End Time', validators=[DataRequired()])
    status = SelectField('Status', choices=[('In Use', 'In Use'), ('In Store', 'In Store')], validators=[DataRequired()])
    submit = SubmitField('Update')

class AddAssetForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    type = SelectField('Type', validators=[DataRequired()],
                        choices=[('harddisk', 'Hard Disk'),
                                 ('testingcard', 'Card')])
    asset_name = StringField('Asset Name', validators=[DataRequired()])
    person_name = StringField('Person', validators=[DataRequired()])
    start_time = DateField('Start Time', validators=[DataRequired()])
    end_time = HiddenField('End Time')
    #status = StringField('Status', validators=[DataRequired()])
    #status = RadioField('Status', choices=[('In Use', 'In Use'), ('In Store', 'In Store')], validators=[DataRequired()])
    status = SelectField('Status', validators=[DataRequired()], choices=[('In Use', 'In Use'), ('In Store', 'In Store')])
    submit = SubmitField('Add')