from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from flask_wtf import Form, FlaskForm
import uuid
import datetime

from . models import Organization, BeneficiaryStakeholder, Impact, Funder, OutcomeReport, db
from . forms import SignUpForm, SignInForm, UserProfileForm, Login, FunderForm, StakeholderForm, Orgregistration, Outregistration

from project import app

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/help', methods=['GET'])
def help():
    return render_template('help.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login = Login()
    return render_template('login.html', form=login)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        reg = User(signupform.firstname.data, signupform.lastname.data,\
         signupform.username.data, signupform.password.data,\
         signupform.email.data)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', signupform=signupform)

# Authentication
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()
    if request.method == 'POST':
        em = signinform.email.data
        log = User.query.filter_by(email=em).first()
        if log.password == signinform.password.data:
            current_user = log.username
            session['current_user'] = current_user
            session['user_available'] = True
            return redirect(url_for('index'))
    return render_template('signin.html', signinform=signinform)

@app.route('/logout')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('index'))

# Organization
@app.route('/organizations')
def show_organizations():
    organizations = Organization.query.all()
    return render_template('organizations.html', organizations=organizations)

@app.route('/orgregistration', methods=['GET', 'POST'])
def orgregistration():
    org = Orgregistration()
    if request.method == 'POST':
        organization = Organization(org.legalName.data, org.description.data, \
        org.useOfFunds.data, org.address.data, org.city.data, org.province.data, org.postalCode.data,\
        org.telephone.data, org.hasContactFirstNameS.data, org.hasContactLastNameS.data, org.hasContactEmails.data, \
        org.hasContactPhoneS.data, org.womanOwned.data, org.indigenousOwned.data, org.blackOwned.data, \
        org.percentIndegenousLeaders.data, org.percentWomenLeaders.data, org.percentBlackLeaders.data, \
        org.percentIndegenousBoard.data, org.percentWomenBoard.data, org.percentBlackBoard.data)
        db.session.add(organization)
        db.session.commit()
        return redirect(url_for('show_organizations'))
    return render_template('orgregistration.html', form=org)

@app.route('/organizations/delete/<identifier>', methods=('GET', 'POST'))
def delete_organization(identifier):
    organization = Organization.query.get(identifier)
    db.session.delete(organization)
    db.session.commit()
    return redirect(url_for('organizations'))

@app.route('/organizations/update/<identifier>', methods=('GET', 'POST'))
def update_organization(identifier):
    org = Organization.query.get(identifier)
    org.name = organization.name.data
    org.description = organization.description.data
    db.session.commit()
    return redirect(url_for('organizations'))

# Funder registration
@app.route('/funders', methods=['GET', 'POST'])
def show_funders():
    funders = Funder.query.all()
    return render_template('funders.html', funders=funders)

@app.route('/funregistration', methods=['GET', 'POST'])
def funregistration():
    fun = FunderForm(request.form)
    if request.method == 'POST':
        funder = Funder(fun.firstname.data, fun.lastname.data, fun.email.data, fun.phone.data, \
        fun.financialinst.data, fun.academicinst.data, fun.govinst.data)
        db.session.add(funder)
        db.session.commit()
        return redirect(url_for('show_funders'))
    return render_template('funregistration.html', form=fun)

@app.route('/funders/update/<identifier>', methods=('GET', 'POST'))
def update_funder(identifier):
    fun = Funder.query.get(identifier)
    funder = FunderForm(obj=fun)
    if request.method == 'POST':
        fun = Funder.query.get(identifier)
        fun.name = funder.name.data
        db.session.commit()
        return redirect(url_for('funders'))
    return render_template('funregistration.html', funder=funder)

# Stakeholder
@app.route('/stakeholders')
def show_stakeholders():
    stakeholders = BeneficiaryStakeholder.query.all()
    return render_template('stakeholders.html', stakeholders=stakeholders)

@app.route('/stkregistration', methods=['GET', 'POST'])
def stkregistration():
    stk = StakeholderForm(request.form)
    if request.method == 'POST':
        stakeholder = BeneficiaryStakeholder(stk.name.data, stk.description.data, stk.location.data, stk.bsMinority.data, \
        stk.bsMentalHealth.data, stk.bsSeniors.data, stk.bsLGBTQ.data, stk.bsNewcomer.data, stk.bsRacialized.data, stk.bsRemote.data, \
        stk.bsDisabilities.data, stk.bsIndigenous.data, stk.bsWomenGirls.data, stk.bsChildrenYouth.data, stk.bsLowIncome.data)
        db.session.add(stakeholder)
        db.session.commit()
        return redirect(url_for('show_stakeholders'))
    return render_template('stkregistration.html', form=stk)

@app.route('/stakeholders/delete/<identifier>', methods=('GET', 'POST'))
def delete_stakeholder(identifier):
    stakeholder = BeneficiaryStakeholder.query.get(identifier)
    db.session.delete(stakeholder)
    db.session.commit()
    return redirect(url_for('stakeholders.html'))

@app.route('/stakeholders/update/<identifier>', methods=('GET', 'POST'))
def update_stakeholder(identifier):
    stkx = BeneficiaryStakeholder.query.get(identifier)
    stakeholder = StakeholderForm(obj=stkx)
    if request.method == 'POST':
        stk = BeneficiaryStakeholder.query.get(org_id)
        stk.name = stakeholder.name.data
        db.session.commit()
        return redirect(url_for('stakeholders'))
    return render_template('stkregistration.html', funder=funder)

# Outcome (Impact)
@app.route('/outcomes', methods=['GET', 'POST'])
def show_outcome():
    outcomes = Impact.query.all()
    return render_template('outcomes.html', outcomes=outcomes)

@app.route('/outregistration', methods=['GET', 'POST'])
def outregistration():
    out = Outregistration()
    if request.method == 'POST':
        name = out.title.data
        description = out.description.data
        forStakeHolder = out.stakeholder1.data
        hasImportance = out.importance.data
        underServed = out.underserved.data
        definedBy = out.sdg1.data
        outcome = Impact(name, description, forStakeHolder, hasImportance, underServed, definedBy)
        db.session.add(outcome)
        db.session.commit()
        return redirect(url_for('outcomes'))
        console.log('Added')
    return render_template('outregistration.html', form=out)

@app.route('/outcomes/update/<identifier>', methods=('GET', 'POST'))
def update_outcome(identifier):
    outx = Impact.query.get(identifier)
    outcome = Outregistration(obj=outx)
    if request.method == 'POST':
        out = Impact.query.get(identifier)
        out.name = outcome.name.data
        db.session.commit()
        return redirect(url_for('outcomes'))
    return render_template('outregistration.html', funder=funder)

@app.route('/reports', methods=['GET', 'POST'])
def outreport():
    outcomereports = OutcomeReport.query.all()
    return render_template('reports.html', outcomereports=outcomereports)

@app.route('/users')
def show_users():
    organizations = Organization.query.all()
    funders = Funder.query.all()
    return render_template('users.html', organizations=organizations, funders=funders)

if __name__ == '__main__':
    app.run()
