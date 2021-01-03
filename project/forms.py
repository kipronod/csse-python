from flask_wtf import Form, FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, StringField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, InputRequired, Optional

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')

class Login(FlaskForm):
    username = StringField('Username', validators=[InputRequired('This field is mandatory')])
    password = StringField('Password', validators=[InputRequired('This field is mandatory')])

class SignUpForm(Form):
    firstname= TextField('First Name', validators= [DataRequired(), length_check])
    lastname = TextField('Last Name', validators= [DataRequired()])
    username = TextField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    submit = SubmitField('Sign Up')

class SignInForm(Form):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')

class UserProfileForm(Form):
    firstname= TextField('First Name', validators= [DataRequired(), length_check])
    lastname = TextField('Last Name', validators= [DataRequired()])
    username = TextField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])

class FunderForm(Form):
    firstname = TextField('First Name', validators= [DataRequired()])
    lastname = TextField('Last Name', validators= [DataRequired()])
    email = TextField('Email', validators= [DataRequired(), Email()])
    phone = TextField('Phone', validators=[ DataRequired(), Length(min=6)])
    financialinst = BooleanField('Financial Institutioin', default=False)
    academicinst = BooleanField('Academic Institution', default=False)
    govinst = BooleanField('Government Institution', default=False)
    submit = SubmitField('Register')

class StakeholderForm(Form):
    name = StringField('Name', validators=[InputRequired('This field is mandatory')])
    description = StringField('Description', validators=[InputRequired('This field is mandatory')])
    location = SelectField('Location', validators=[InputRequired('This field is mandatory')], choices = [(''),('Regional'),('National')], validate_choice=True)
    bsMinority = BooleanField('Official Language Minority Communities', validators=[Optional()])
    bsMentalHealth = BooleanField('Living with mental health/additions', validators=[Optional()])
    bsSeniors = BooleanField('Seniors', validators=[Optional()])
    bsLGBTQ = BooleanField('LGBTQS+', validators=[Optional()])
    bsNewcomer = BooleanField('Newcomers and Refugees', validators=[Optional()])
    bsRacialized = BooleanField('Racialized(all)', validators=[Optional()])
    bsRemote = BooleanField('Rural, Remote or Northern Community', validators=[Optional()])
    bsDisabilities = BooleanField('People with disabilities', validators=[Optional()])
    bsIndigenous = BooleanField('Indigenous', validators=[Optional()])
    bsWomenGirls = BooleanField('Women and Girls', validators=[Optional()])
    bsChildrenYouth = BooleanField('Children and Youth', validators=[Optional()])
    bsLowIncome = BooleanField('Low Income', validators=[Optional()])

class Orgregistration(FlaskForm):
    orgbusnum = StringField('Organization Business Number', validators=[InputRequired('This field is mandatory'), Length(min=9, max=9, message='Your Organization Business Number is exactly 9 digits')])
    legalName = StringField('Legal Name', validators=[InputRequired('This field is mandatory')])
    description = StringField('Description', validators=[InputRequired('This field is mandatory')])
    useOfFunds = StringField('Use of Funds', validators=[InputRequired('This field is mandatory')])
    address = StringField('Street Number and Name', validators=[InputRequired('This field is mandatory')])
    city = StringField('City', validators=[InputRequired('This field is mandatory')])
    province = SelectField('Province', validators=[InputRequired('This field is mandatory')], choices = [(''),('ON'),('QC')], validate_choice=True)
    postalCode = StringField('Postal Code', validators=[InputRequired('This field is mandatory')])
    telephone = StringField('Phone', validators=[InputRequired('This field is mandatory'), Length(min=10, max=10, message='Your phone number is exactly 10 digits including country code ')])
    hasContactFirstNameS = StringField('First Name', validators=[InputRequired('This field is mandatory')])
    hasContactLastNameS = StringField('Last Name', validators=[InputRequired('This field is mandatory')])
    hasContactEmails = StringField('Email', validators=[InputRequired('This field is mandatory'), Email()])
    hasContactPhoneS = StringField('Phone', validators=[InputRequired('This field is mandatory'), Length(min=10, max=10, message='Your phone number is exactly 10 digits including country code ')])
    womanOwned = BooleanField('Women Owned', validators=[Optional()], default=False)
    indigenousOwned = BooleanField('Aboriginal Owned', validators=[Optional()], default=False)
    blackOwned = BooleanField('Black Owned', validators=[Optional()], default=False)
    percentIndegenousLeaders = IntegerField('Percent of Indigenous, Inuit or Metis Leaders', validators=[InputRequired('This field is mandatory')])
    percentWomenLeaders = IntegerField('Percent of Women Leaders', validators=[InputRequired('This field is mandatory')])
    percentBlackLeaders = IntegerField('Percent of Black Leaders', validators=[InputRequired('This field is mandatory')])
    percentIndegenousBoard = IntegerField('Percent of Indigenous, Inuit or Metis', validators=[InputRequired('This field is mandatory')])
    percentWomenBoard = IntegerField('Percent of Women Owned', validators=[InputRequired('This field is mandatory')])
    percentBlackBoard = IntegerField('Percent of Black Owned', validators=[InputRequired('This field is mandatory')])

class Outregistration(FlaskForm):
    title = StringField('Title', validators=[InputRequired('This field is mandatory')])
    description = StringField('Description', validators=[InputRequired('This field is mandatory')])
    sdg1 = SelectField('UN SDG', validators=[InputRequired('This field is mandatory')], choices = [(''), ('No Poverty'), ('Zero Hunger')], validate_choice=True)
    sdg2 = SelectField('UN SDG', validators=[InputRequired('This field is mandatory')], choices = [(''), ('No Poverty'), ('Zero Hunger')], validate_choice=True)
    stakeholder1 = SelectField('Stakeholder Involved', validators=[InputRequired('This field is mandatory')], choices = [(''), ('stakeholder 1'), ('Stakeholder 2')], validate_choice=True)
    importance = SelectField('Importance', validators=[InputRequired('This field is mandatory')], choices = [(''), ('neutral'), ('unimportant')], validate_choice=True)
    underserved = BooleanField('Underserved', validators=[Optional()])
    stakeholder2 = SelectField('Stakeholder Involved', validators=[InputRequired('This field is mandatory')], choices = [(''), ('stakeholder 1'), ('Stakeholder 2')], validate_choice=True)
    importance2 = SelectField('Importance', validators=[InputRequired('This field is mandatory')], choices = [(''), ('neutral'), ('unimportant')], validate_choice=True)
    underserved2 = BooleanField('Underserved', validators=[Optional()])
    indicatorname = StringField('Name', validators=[InputRequired('This field is mandatory')])
    indicatordescription = StringField('Description', validators=[InputRequired('This field is mandatory')])
    baseline = IntegerField('Baseline', validators=[InputRequired('This field is mandatory')])
    threshold = IntegerField('Threshold', validators=[InputRequired('This field is mandatory')])
    exists = SelectField('Exists', validators=[InputRequired('This field is mandatory')], choices = [(''),('Yes'),('No')], validate_choice=True)
    probability = IntegerField('Probability', validators=[InputRequired('This field is mandatory')])
    riskdescription = StringField('Description', validators=[InputRequired('This field is mandatory')])