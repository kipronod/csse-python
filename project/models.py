from flask_sqlalchemy import SQLAlchemy
import datetime
from project import app

db = SQLAlchemy(app)

class Funder(db.Model):
    identifier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    phone = db.Column(db.String(50))
    financialinst = db.Column(db.Boolean, unique=False, default=False)
    academicinst = db.Column(db.Boolean, unique=False, default=False)
    govinst = db.Column(db.Boolean, unique=False, default=False)
    
    def __init__(self, identifier, firstname, email, username, phone, financialinst, academicinst, govinst):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.financialinst = financialinst
        self.academicinst = academicinst
        self.govinst = govinst
        
class Organization(db.Model):
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    legalName = db.Column('sch:legalName', db.String(100))
    description = db.Column('sch:description', db.String(100))
    useOfFunds = db.Column('sch:useOfFunds', db.String(100))
    telephone = db.Column('sch:telephone', db.String(100))
    email = db.Column('sch:email', db.String(100))
    address = db.Column('sch:address', db.String(100))
    city = db.Column('city', db.String(100))
    country = db.Column('addressCountry', db.String(100), default='Canada')
    postalCode = db.Column('postalCode', db.String(100))
    province = db.Column('province', db.String(100))
    hasContactEmails = db.Column('hasContactEmails', db.String(1000))
    hasContactFirstNameS = db.Column('hasContactFirstNameS', db.String(1000))
    hasContactLastNameS = db.Column('hasContactLastNameS', db.String(1000))
    hasContactPhoneS = db.Column('hasContactPhoneS', db.String(1000))
    percentBlackBoard = db.Column('percentBlackBoard', db.Integer)
    percentBlackLeaders = db.Column('percentBlackLeaders', db.Integer)
    percentIndegenousBoard = db.Column('percentIndegenousBoard', db.Integer)
    percentIndegenousLeaders = db.Column('percentIndegenousLeaders', db.Integer)
    percentWomenBoard = db.Column('percentWomenBoard', db.Integer)
    percentWomenLeaders = db.Column('percentWomenLeaders', db.Integer)
    blackOwned = db.Column(db.Boolean, unique=False, default=False)
    indigenousOwned = db.Column(db.Boolean, unique=False, default=False)
    womanOwned = db.Column(db.Boolean, unique=False, default=False)
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)

    def __init__(self, identifier, legalName, memberOf, description, address, telephone, email, hasOutcomeS, hasIndicatorS, hasIndicatorReportS, dateCreated, provider):
        self.identifier = identifier
        self.legalName = legalName
        self.memberOf = memberOf
        self.description = description
        self.address = address
        self.telephone = telephone
        self.hasContactS = hasContactS
        self.email = email
        self.hasIndicatorS = hasIndicatorS
        self.hasIndicatorReportS = hasIndicatorReportS
        self.dateCreated = dateCreated
        self.provider = provider

class Impact(db.Model):
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('sch:name', db.String(100))
    description = db.Column('sch:description', db.String(1000))
    forStakeHolder = db.Column('forStakeHolder', db.String(1000))
    hasImportance = db.Column('hasImportance', db.String(1000))
    underServed = db.Column('underServed', db.String(1000))
    definedBy = db.Column('definedBy', db.String(1000))
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    provider = db.Column('sch:provider', db.String(100))

    def __init__(self, identifier, name, description, forStakeHolder, hasImportance, underServed, definedBy, dateCreated, provider):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.forStakeHolder = forStakeHolder
        self.hasImportance = hasImportance
        self.underServed = underServed
        self.definedBy = definedBy
        self.dateCreated = dateCreated
        self.provider = provider

class Indicator(db.Model):
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('sch:name', db.String(100))
    description = db.Column('sch:description', db.String(1000))
    defineByS = db.Column('defineByS', db.String(1000))
    forOutcomeS = db.Column('forOutcomeS', db.String(1000))
    hasSimilarIndicatorS = db.Column('hasSimilarIndicatorS', db.String(1000))
    hasIndicatorReportS = db.Column('hasIndicatorReportS', db.String(1000))
    hasThresholdS = db.Column('hasThresholdS', db.String(1000))
    hasBaselineS = db.Column('hasBaselineS', db.String(1000))
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    provider = db.Column('sch:provider', db.String(100))

    def __init__(self, identifier, name, description, defineByS, forOutcomeS, hasSimilarIndicatorS, hasIndicatorReportS, hasThresholdS, hasBaselineS, dateCreated, provider):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.defineByS = defineByS
        self.forOutcomeS = forOutcomeS
        self.hasSimilarIndicatorS = hasSimilarIndicatorS
        self.hasIndicatorReportS = hasIndicatorReportS
        self.hasThresholdS = hasThresholdS
        self.hasBaselineS = hasBaselineS
        self.dateCreated = dateCreated
        self.provider = provider

class IndicatorReport(db.Model):
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('sch:name', db.String(100))
    forOrganization = db.Column('forOrganization', db.String(1000))
    forOutcome = db.Column('forOutcome', db.String(1000))
    forIndicator = db.Column('forIndicator', db.String(1000))
    forStartDate = db.Column('forStartDate', db.String(1000))
    forEndDate = db.Column('forEndDate', db.String(1000))
    hasValue = db.Column('hasValue', db.String(1000))
    hasComment = db.Column('hasComment', db.String(1000))
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    provider = db.Column('sch:provider', db.String(100))

    def __init__(self, identifier, name, forOrganization, forOutcome, forIndicator, forStartDate, forEndDate, hasValue, hasComment, dateCreated, provider):
        self.identifier = identifier
        self.name = name
        self.forOrganization = forOrganization
        self.forOutcome = forOutcome
        self.forIndicator = forIndicator
        self.forStartDate = forStartDate
        self.forEndDate = forEndDate
        self.hasValue = hasValue
        self.hasComment = hasComment
        self.dateCreated = dateCreated
        self.provider = provider

class OutcomeReport(db.Model):
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('sch:name', db.String(100))
    forOrganization = db.Column('forOrganization', db.String(1000))
    forOutcome = db.Column('forOutcome', db.String(1000))
    hasExpectation = db.Column('hasExpectation', db.String(1000))
    hasScaleValue = db.Column('hasScaleValue', db.String(1000))
    hasScaleCFValueS = db.Column('hasScaleCFValueS', db.String(1000))
    hasScaleCFSource = db.Column('hasScaleCFSource', db.String(1000))
    hasDepthIndicator = db.Column('hasDepthIndicator', db.String(1000))
    hasDepthValue = db.Column('hasDepthValue', db.String(1000))
    hasDepthCFValue = db.Column('hasDepthCFValue', db.String(1000))
    hasDepthCFSource = db.Column('hasDepthCFSource', db.String(1000))
    hasDurationStartDate = db.Column('hasDurationStartDate', db.String(1000))
    hasDurationEndDate = db.Column('hasDurationEndDate', db.String(1000))
    hasDurationCFValue = db.Column('hasDurationCFValue', db.String(1000))
    hasDurationCFSource = db.Column('hasDurationCFSource', db.String(1000))
    hasOutcomeComment = db.Column('hasOutcomeComment', db.String(1000))
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    provider = db.Column('sch:provider', db.String(100))

    def __init__(self, identifier, name, forOrganization, forOutcome, hasExpectation, hasScaleValue, hasScaleCFValueS, hasScaleCFSource, hasDepthIndicator, hasDepthValue, hasDepthCFValue, hasDepthCFSource, hasDurationStartDate, hasDurationEndDate, hasDurationCFValue, hasDurationCFSource, hasOutcomeComment, dateCreated, provider):
        self.identifier = identifier
        self.name = name
        self.forOrganization = forOrganization
        self.forOutcome = forOutcome
        self.hasExpectation = hasExpectation
        self.hasScaleValue = hasScaleValue
        self.hasScaleCFValueS = hasScaleCFValueS
        self.hasScaleCFSource = hasScaleCFSource
        self.hasDepthIndicator = hasDepthIndicator
        self.hasDepthValue = hasDepthValue
        self.hasDepthCFValue = hasDepthCFValue
        self.hasDepthCFSource = hasDepthCFSource
        self.hasDurationStartDate = hasDurationStartDate
        self.hasDurationEndDate = hasDurationEndDate
        self.hasDurationCFValue = hasDurationCFValue
        self.hasDurationCFSource = hasDurationCFSource
        self.hasOutcomeComment = hasOutcomeComment
        self.dateCreated = dateCreated
        self.provider = provider

class BeneficiaryStakeholder(db.Model):
    subClassOf = db.Column('subClassOf', db.String(100))
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('sch:name', db.String(100))
    description = db.Column('sch:description', db.String(1000))
    location = db.Column('location', db.String(1000))
    bsMinority = db.Column('bsMinority', db.String(1000))
    bsMentalHealth = db.Column('bsMentalHealth', db.String(1000))
    bsSeniors = db.Column('bsSeniors', db.String(1000))
    bsLGBTQ = db.Column('bsLGBTQ', db.String(1000))
    bsNewcomer = db.Column('bsNewcomer', db.String(1000))
    bsRacialized = db.Column('bsRacialized', db.String(1000))
    bsRemote = db.Column('bsRemote', db.String(1000))
    bsDisabilities = db.Column('bsDisabilities', db.String(1000))
    bsIndigenous = db.Column('bsIndigenous', db.String(1000))
    bsWomenGirls = db.Column('bsWomenGirls', db.String(1000))
    bsChildrenYouth = db.Column('bsChildrenYouth', db.String(1000))
    bsLowIncome = db.Column('bsLowIncome', db.String(1000))
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    provider = db.Column('sch:provider', db.String(100))

    def __init__(self, subClassOf, identifier, name, description, location, bsMinority, bsMentalHealth, bsSeniors, bsLGBTQ, bsNewcomer, bsRacialized, bsRemote, bsDisabilities, bsIndigenous, bsWomenGirls, bsChildrenYouth, bsLowIncome, dateCreated, provider):
        self.subClassOf = subClassOf
        self.identifier = identifier
        self.name = name
        self.description = description
        self.location = location
        self.bsMinority = bsMinority
        self.bsMentalHealth = bsMentalHealth
        self.bsSeniors = bsSeniors
        self.bsLGBTQ = bsLGBTQ
        self.bsNewcomer = bsNewcomer
        self.bsRacialized = bsRacialized
        self.bsRemote = bsRemote
        self.bsDisabilities = bsDisabilities
        self.bsIndigenous = bsIndigenous
        self.bsWomenGirls = bsWomenGirls
        self.bsChildrenYouth = bsChildrenYouth 
        self.bsLowIncome = bsLowIncome
        self.dateCreated = dateCreated
        self.provider = provider
        
class SimilarIndicator(db.Model):
    identifier = db.Column('sch:identifier', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('sch:name', db.String(100))
    description = db.Column('sch:description', db.String(1000))
    forIndicatorS = db.Column('forIndicatorS', db.String(1000))
    definedBy = db.Column('definedBy', db.String(1000))
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    provider = db.Column('sch:provider', db.String(100))

    def __init__(self, identifier, name, description, forIndicatorS, definedBy, dateCreated, provider):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.forIndicatorS = forIndicatorS
        self.definedBy = definedBy
        self.dateCreated = dateCreated
        self.provider = provider

db.create_all()