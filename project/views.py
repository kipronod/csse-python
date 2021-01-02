from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from flask_wtf import Form, FlaskForm
import uuid

from . models import Organization, BeneficiaryStakeholder, Impact, Funder, db
from . forms import SignUpForm, SignInForm, UserProfileForm, Login, FunderForm, Orgregistration, Stkregistration, Outregistration

from project import app

@app.route('/')
def index():
    return render_template('index.html')

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
        org.percentIndegenousBoard.data, org.percentWomenBoard.data, org.percentBlackBoard.data \
        )
        db.session.add(organization)
        db.session.commit()
        return redirect(url_for('index'))
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

# Stakeholder
@app.route('/stakeholders')
def show_stakeholders():
    stakeholders = BeneficiaryStakeholder.query.all()
    return render_template('', stakeholders=stakeholders)

@app.route('/stkregistration', methods=['GET', 'POST'])
def stkregistration():
    stk = Stkregistration(request.form)
    if request.method == 'POST':
        name = stk.title.data
        description = stk.description.data
        location = stk.location.data
        bsMinority = stk.offlangmincom.data
        bsMentalHealth = stk.mentalhealth.data
        bsSeniors = stk.seniors.data
        bsLGBTQ = stk.queer.data
        bsNewcomer = stk.newref.data
        bsRacialized = stk.racial.data
        bsRemote = stk.community.data
        bsDisabilities = stk.disability.data
        bsIndigenous = stk.indi.data
        bsWomenGirls = stk.female.data
        bsChildrenYouth = stk.child.data
        bsLowIncome = stk.lowincome.data
        stakeholder = BeneficiaryStakeholder(name, description, location, bsMinority, bsMentalHealth, bsSeniors, bsLGBTQ, \
        bsNewcomer, bsNewcomer, bsRacialized, bsRemote, bsDisabilities, bsIndigenous, bsWomenGirls, bsChildrenYouth, bsLowIncome)
        db.session.add(stakeholder)
        db.session.commit()
        return redirect(url_for('stakeholders'))
        console.log('Added')
    return render_template('stkregistration.html', form=stk)

@app.route('/stakeholders/delete/<identifier>', methods=('GET', 'POST'))
def delete_stakeholder(identifier):
    stakeholder = BeneficiaryStakeholder.query.get(identifier)
    db.session.delete(stakeholder)
    db.session.commit()
    return redirect(url_for('stakeholders'))

@app.route('/stakeholders/update/<identifier>', methods=('GET', 'POST'))
def update_stakeholder(identifier):
    stkx = BeneficiaryStakeholder.query.get(identifier)
    stakeholder = Stkregistration(obj=stkx)
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
    return render_template('', outcomes=outcomes)

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

# Funder registration
@app.route('/funders', methods=['GET', 'POST'])
def show_funders():
    funders = Funder.query.all()
    print(funders)
    return render_template('funders.html', funders=funders)

@app.route('/funregistration', methods=['GET', 'POST'])
def funregistration():
    fun = FunderForm(request.form)
    if request.method == 'POST':
        identifier = 'ORG' + str(uuid.uuid4())[:8]
        firstname = fun.firstname.data
        lastname = fun.lastname.data
        email = fun.email.data
        phone = fun.phone.data
        financialinst = fun.financialinst.data
        academicinst = fun.academicinst.data
        govinst = fun.govinst.data
        funder = Funder(firstname, lastname, email, phone, financialinst, academicinst, govinst)
        db.session.add(funder)
        db.session.commit()
        return redirect(url_for(show_funders))
        print('Added')
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

if __name__ == '__main__':
    app.run()
