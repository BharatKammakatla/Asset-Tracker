from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, ValidationError, DateField
from wtforms.validators import DataRequired
# from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from app.asset.models import Asset


def check_if_asset_exist(form, field):
    asset = Asset.query.filter_by(asset_name=field.data).first()
    if asset:
        raise ValidationError('Asset Already Exists')


def get_assets():
    return Asset.query.all()


class EditTransactionForm(FlaskForm):
    type = StringField('Type', render_kw={'readonly': True})
    asset_name = StringField('Asset Name', render_kw={'readonly': True})
    person_name = StringField('Person', render_kw={'readonly': True})
    start_time = DateField('Start Time', render_kw={'readonly': True})
    # end_time = DateField('End Time', validators=[DataRequired()])
    end_time = DateField('End Time', validators=[DataRequired()], format='%m/%d/%y',
                         render_kw={'placeholder': '6/20/15 for June 20, 2015'})
    status = SelectField('Status', choices=[('In Use', 'In Use'), ('In Store', 'In Store')],
                         validators=[DataRequired()])
    submit = SubmitField('Update')


class AddTransactionForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('harddisk', 'Hard Disk'), ('testingcard', 'Card')])
    asset_name = QuerySelectField(label='Asset Name', validators=[DataRequired()], query_factory=get_assets,
                                  allow_blank=True)
    person_name = StringField('Person', validators=[DataRequired()])
    # start_time = DateField('Start Time', validators=[DataRequired()])
    start_time = DateField('Start Time', format='%m/%d/%y', render_kw={'placeholder': '6/20/15 for June 20, 2015'})
    end_time = HiddenField('End Time')
    status = SelectField('Status', validators=[DataRequired()], choices=[('In Use', 'In Use')])
    submit = SubmitField('Add')


class AddAssetForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('harddisk', 'Hard Disk'),
                                ('testingcard', 'Card')])
    asset_name = StringField('Asset Name', validators=[DataRequired(), check_if_asset_exist])
    submit = SubmitField('Register')
