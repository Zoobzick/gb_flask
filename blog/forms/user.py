from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()])
    email = StringField("Email Adress", [
                        validators.DataRequired(),
                        validators.Email(),
                        validators.Length(min=6, max=50)],
                        filters=[lambda data: data and data.lower()])


class RegistrationForm(UserBaseForm):
    password = PasswordField(
        "New Password", [validators.data_required(),
                         validators.EqualTo("confirm", message="Passwords must match")])
    confirm = PasswordField("Repeat password")
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "email",
        [validators.DataRequired(),
         validators.Email(),
         validators.Length(min=6, max=50)],
    )
    password = PasswordField(
        "Password",
        [validators.DataRequired()],
    )
    submit = SubmitField("Login")
