from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
import application

class RegisterForm_Student(FlaskForm):
    def validate_username(self, student_to_check):

        student = application.User.query.filter_by(username=student_to_check.data).first()
        if student:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = application.User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    roll_number = IntegerField(label='Roll Number:', validators=[DataRequired()])
    name = StringField(label='Name:', validators=[Length(min=2, max=50), DataRequired()])
    stream = StringField(label='Stream:', validators=[Length(min=1, max=50), DataRequired()])
    d_o_b = StringField(label='Date of Birth(DD/MM/YYYY):', validators=[Length(min=2, max=50), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class RegisterForm_Admin(FlaskForm):
    def validate_username(self, admin_to_check):

        admin = application.User.query.filter_by(username=admin_to_check.data).first()
        if admin:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = application.User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    admin_id = IntegerField(label='ID:', validators=[DataRequired()])
    admin_name = StringField(label='Name:', validators=[Length(min=2, max=50), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm_Student(FlaskForm):
    roll_number = IntegerField(label='Roll Number:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class LoginForm_Admin(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')



class add_attend(FlaskForm):
    roll_number = IntegerField(label='Roll Number:', validators=[DataRequired()])
    course = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    total_days = IntegerField(label='Total Days:', validators=[DataRequired()])
    present = IntegerField(label='No of days present:', validators=[DataRequired()])
    comments = StringField(label='Comments:', validators=[Length(min=2, max=50), DataRequired()])
    submit = SubmitField(label='Add')


class add_course(FlaskForm):
    roll = IntegerField(label='Roll Number:', validators=[DataRequired()])
    faculty_id = IntegerField(label='Faculty ID:', validators=[DataRequired()])
    faculty_name = StringField(label='Faculty Name:', validators=[Length(min=2, max=50), DataRequired()])
    course_name = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    faculty_email = StringField(label='Faculty Email:', validators=[Length(min=2, max=50), DataRequired()])
    faculty_mobile = StringField(label='Faculty Mobile:', validators=[Length(min=2, max=12), DataRequired()])
    submit = SubmitField(label='Add')


class add_ttable(FlaskForm):
    roll =  IntegerField(label='Roll Number:', validators=[DataRequired()])
    course1 = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    course2 = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    course3 = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    course4 = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    course5 = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    course6 = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    days = StringField(label='Day:', validators=[Length(min=2, max=50), DataRequired()])
    submit = SubmitField(label='Add')


class add_result(FlaskForm):
    roll_number = IntegerField(label='Roll Number:', validators=[DataRequired()])
    course_name = StringField(label='Course Name:', validators=[Length(min=2, max=50), DataRequired()])
    grade = StringField(label='Grade:', validators=[Length(max=5), DataRequired()])
    sgpa = StringField(label='Sgpa:', validators=[Length(max=5), DataRequired()])
    submit = SubmitField(label='Add')


class add_fee(FlaskForm):
    id = IntegerField(label='Roll Number:', validators=[DataRequired()])
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    amount = IntegerField(label='Amount:', validators=[DataRequired()])
    fees_desc = StringField(label='Description:', validators=[Length(min=2, max=1024), DataRequired()])
    submit = SubmitField(label='Add')
