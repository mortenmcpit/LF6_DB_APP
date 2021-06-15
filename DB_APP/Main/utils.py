from DB_APP.Main.models import *
from sqlalchemy import func
import random
from random import randint


class Themenwoche1:

    def kundennummer(self):
        doppelt = True
        while doppelt:

            output = "KD"
            temp_310 = ""
            templast = ""
            tempintlast = 0

            for i in range(8):
                schtemp = randint(0, 9)
                tempintlast += schtemp
                temp_310 += str(schtemp)

            if tempintlast <= 9:
                templast = "0" + str(tempintlast)
            else:
                templast = str(tempintlast)

            output += temp_310 + templast
            doppelt = self.finde_Kundennummer(output)
        return output

    def finde_Kundennummer(self, checknummber):
        return False

    def fehler1(self, input):
        for i in input:
            fehler = True
            for x in range(10):
                if i == str(x):
                    fehler = False
                if x == 9 and fehler:
                    return 1

        if not (fehler):
            return 0

    def fehler2(self, input):
        netto = ""
        brutto = ""
        i = 1

        for zeichen in input:
            if i > 8 and i < 15:
                netto += zeichen
            if i > 18:
                brutto += zeichen
            i += 1

        if (int(netto) > int(brutto)):
            return 2
        else:
            return 0

    def Barcode(self, input):
        felhler = 0
        felhler = self.fehler1(input)
        if felhler == 0:
            felhler = self.fehler2(input)
        return felhler


test = Themenwoche1()


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

# Function to automatically generate new ordernumber
def ordernumgenerator():
    pass


# Functions to get all entries from objects
def articles():
    return Article.query.all()


def orders():
    return Order.query.all()


def persons():
    return Person.query.all()


def producers():
    return Producer.query.all()
