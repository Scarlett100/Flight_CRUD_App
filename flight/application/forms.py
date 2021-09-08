from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateTimeField, BooleanField, DecimalField, DateField
from wtforms.validators import DataRequired, ValidationError, Length

from application.models import Aeroplanes
from application.models import Flights

class AeroplanesForm(FlaskForm):
    model_number = SelectField("model", choices=[(747, 747),
    (812, 812),
    (989, 989)
    ])
    number_of_seats = SelectField("number of seats", choices=[
        (40, 40),
        (90, 90), 
        (173, 173)
    ])
    company_owned_by = SelectField("owner", choices=[
        ("Emirates", "Emirates"), 
        ("British Airways", "British Airways"), 
        ("Virgin Atlantic", "Virgin Atlantic"), 
        ("Air France", "Air France")
    ])
    

    submit = SubmitField('Submit')


class FlightsForm(FlaskForm):
    departure_date_time = DateField("departure date YYYY-MM-DDH:M:S",format="%Y-%m-%d",
        validators=[DataRequired()])

    arrival_date_time= DateField("arrival date & time YYY-MM-DDH:M:S",format="%Y-%m-%d")
    arrival_destination = StringField("arrival",
        validators=[DataRequired(), Length(min=2, max=30)])
    direct_flight = BooleanField("direct flight") #selectfield? yes or no
    flight_price = DecimalField("budget (eg. 500 = £500)",
        validators=[DataRequired()])
    fk_aeroplane_id = IntegerField()

    submit = SubmitField("Submit")

