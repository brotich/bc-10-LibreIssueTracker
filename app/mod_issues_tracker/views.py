from wtforms import Form, StringField, SelectField, TextAreaField
from wtforms import RadioField

from app.models import Department, User


class NewIssueForm(Form):
    title = StringField("Title")
    department = SelectField(label="Department", choices=Department().get_departments())
    priority = RadioField(label="priority", choices=[
        ("low", "low"), ("medium", "medium"), ("high", "high")
    ])
    description = TextAreaField(label="Description")


class AssignIssueForm(Form):
    users = SelectField(label="User", choices=User().get_users())
    comment = TextAreaField(label="comments")
