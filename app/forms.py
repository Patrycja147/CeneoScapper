from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ProductForm(FlaskForm):
    product_id=StringField(
        "Podaj kod produktu z serwisu Ceneo.pl",
        validators=[
            DataRequired("Musisz podać kod produktu"),
            Length(min=6, max=8, message="Kod produktu jest za krótki lub za długi"),
            Regexp("^[0-9]{8}$",message="Kod produktu może zawierać tylko cyfry!")
        ]
    )
    submit = SubmitField("Pobierz")