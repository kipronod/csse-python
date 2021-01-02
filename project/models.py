from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid
from project import app

db = SQLAlchemy(app)

class Funder(db.Model):
    __tablename__ = "Funder"
    identifier = db.Column(db.String(100), primary_key=True, default='FUN' + str(uuid.uuid4())[:8])
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, index=True)
    phone = db.Column(db.String(100))
    financialinst = db.Column(db.Boolean, default=False)
    academicinst = db.Column(db.Boolean, default=False)
    govinst = db.Column(db.Boolean, default=False)
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)
    
    def __init__(self, firstname, lastname, email, username, phone, financialinst, academicinst, govinst):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.financialinst = financialinst
        self.academicinst = academicinst
        self.govinst = govinst
        
class Organization(db.Model):
    __tablename__ = "Organization"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='ORG' + str(uuid.uuid4())[:8])
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

    def __init__(self, legalName, description, useOfFunds, address, city, province, postalCode, \
    telephone, hasContactFirstNameS, hasContactLastNameS, hasContactEmails, hasContactPhoneS, womanOwned, \
    indigenousOwned, blackOwned, percentIndegenousLeaders, percentWomenLeaders, percentBlackLeaders, \
    percentIndegenousBoard, percentWomenBoard, percentBlackBoard):
        self.legalName = legalName
        self.description = description
        self.useOfFunds = useOfFunds
        self.address = address
        self.city = city
        self.province = province
        self.postalCode = postalCode
        self.telephone = telephone
        self.hasContactFirstNameS = hasContactFirstNameS
        self.hasContactLastNameS = hasContactLastNameS
        self.hasContactEmails = hasContactEmails
        self.hasContactPhoneS = hasContactPhoneS
        self.womanOwned = womanOwned
        self.indigenousOwned = indigenousOwned
        self.blackOwned = blackOwned
        self.percentIndegenousLeaders = percentIndegenousLeaders
        self.percentWomenLeaders = percentWomenLeaders
        self.percentBlackLeaders = percentBlackLeaders
        self.percentIndegenousBoard = percentIndegenousBoard
        self.percentWomenBoard = percentWomenBoard
        self.percentBlackBoard = percentBlackBoard

class Impact(db.Model):
    __tablename__ = "Impact"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='OUT' + str(uuid.uuid4())[:8])
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
    __tablename__ = "Indicator"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='IND' + str(uuid.uuid4())[:8])
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
    __tablename__ = "IndicatorReport"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='INR' + str(uuid.uuid4())[:8])
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
    __tablename__ = "OutcomeReport"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='OUT' + str(uuid.uuid4())[:8])
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

    def __init__(self, name, forOrganization, forOutcome, hasExpectation, hasScaleValue, \
    hasScaleCFValueS, hasScaleCFSource, hasDepthIndicator, hasDepthValue, hasDepthCFValue, \
    hasDepthCFSource, hasDurationStartDate, hasDurationEndDate, hasDurationCFValue, \
    hasDurationCFSource, hasOutcomeComment, dateCreated, provider):
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
    __tablename__ = "BeneficiaryStakeholder"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='STK' + str(uuid.uuid4())[:8])
    subClassOf = db.Column('subClassOf', db.String(100), nullable=True)
    name = db.Column('sch:name', db.String(100))
    description = db.Column('sch:description', db.String(1000))
    location = db.Column('location', db.String(1000))
    bsMinority = db.Column(db.Boolean, default=False)
    bsMentalHealth = db.Column(db.Boolean, default=False)
    bsSeniors = db.Column(db.Boolean, default=False)
    bsLGBTQ = db.Column(db.Boolean, default=False)
    bsNewcomer = db.Column(db.Boolean, default=False)
    bsRacialized = db.Column(db.Boolean, default=False)
    bsRemote = db.Column(db.Boolean, default=False)
    bsDisabilities = db.Column(db.Boolean, default=False)
    bsIndigenous = db.Column(db.Boolean, default=False)
    bsWomenGirls = db.Column(db.Boolean, default=False)
    bsChildrenYouth = db.Column(db.Boolean, default=False)
    bsLowIncome = db.Column(db.Boolean, default=False)
    dateCreated = db.Column('sch:dateCreated', db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, description, location, bsMinority, bsMentalHealth, \
    bsSeniors, bsLGBTQ, bsNewcomer, bsRacialized, bsRemote, bsDisabilities, bsIndigenous, bsWomenGirls, \
    bsChildrenYouth, bsLowIncome):
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
        
class SimilarIndicator(db.Model):
    __tablename__ = "SimilarIndicator"
    identifier = db.Column('sch:identifier', db.String(100), primary_key=True, default='SIM' + str(uuid.uuid4())[:8])
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