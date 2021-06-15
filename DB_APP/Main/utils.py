from DB_APP.Main.models import *
from sqlalchemy import func


# Functions to automatically generate new primary keys
def articlenumgenerator():
    highest = db.session.query(func.max(Article.articlenumber).label('integer')).one()
    last_num = Article.query.filter_by(articlenumber=highest.integer).first()
    id_num = last_num.articlenumber
    return id_num + 1


def producernumgenerator():
    highest = db.session.query(func.max(Producer.producernumber).label('integer')).one()
    last_num = Producer.query.filter_by(producernumber=highest.integer).first()
    id_num = last_num.producernumber
    return id_num + 1


def customernumgenerator():
    highest = db.session.query(func.max(Person.personnumber).label('integer')).one()
    last_num = Person.query.filter_by(personnumber=highest.integer).first()
    id_num = last_num.personnumber
    return id_num + 1


def ordernumgenerator():
    highest = db.session.query(func.max(Order.ordernumber).label('integer')).one()
    last_num = Order.query.filter_by(ordernumber=highest.integer).first()
    id_num = last_num.ordernumber
    return id_num + 1


# Functions to get all entries from objects
def articles():
    return Article.query.all()


def orders():
    return Order.query.all()


def persons():
    return Person.query.all()


def producers():
    return Producer.query.all()
