from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class GenderForm(FlaskForm):
    gender = SelectField('Select Gender',
        choices=[('Female', 'Female'), ('Male', 'Male')],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Generate!')