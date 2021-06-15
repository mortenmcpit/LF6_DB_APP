from DB_APP import db


# DB Tabelle 'Person'
class Person(db.Model):
    __tablename__ = 'person'
    personnumber = db.Column('personennummer', db.Integer, primary_key=True, autoincrement=True)
    lastname = db.Column('nachname', db.String(20))
    firstname = db.Column('vorname', db.String(20))
    street = db.Column('strasse', db.String(30))
    place = db.Column('ort', db.String(30))
    zipcode = db.Column('plz', db.Integer())
    country = db.Column('land', db.String(20))
    birthday = db.Column('geburtsdatum', db.Date())

    def __repr__(self):
        return f'{self.lastname}, {self.firstname}'


# DB Tabelle 'Hersteller'
class Producer(db.Model):
    __tablename__ = 'hersteller'
    producernumber = db.Column('herstellernummer', db.Integer(), primary_key=True, autoincrement=True)
    producername = db.Column('herstellername', db.String(30))
    country = db.Column('land', db.String(30))

    def __repr__(self):
        return f'{self.producername}'


# DB Tabelle 'Artikel'
class Article(db.Model):
    __tablename__ = 'artikel'
    articlenumber = db.Column('artikelnummer', db.Integer, primary_key=True, autoincrement=True)
    producernumber = db.Column('herstellernummer', db.Integer, db.ForeignKey(Producer.producernumber))
    articlename = db.Column('artikelname', db.String())
    price = db.Column('preis', db.Float())

    producer = db.relationship(Producer, lazy=True)

    def __repr__(self):
        return f'{self.articlename}'


# DB Tabelle 'Bestellungen'
class Order(db.Model):
    __tablename__ = 'bestellung'
    ordernumber = db.Column('bestellnummer', db.Integer(), primary_key=True, autoincrement=True)
    articlenumber = db.Column('artikelnummer', db.Integer(), db.ForeignKey(Article.articlenumber))
    customernumber = db.Column('kundennummer', db.Integer(), db.ForeignKey(Person.personnumber))
    articlequantity = db.Column('artikelanzahl', db.Integer())
    ordersum = db.Column('bestellsumme', db.Float())

    article = db.relationship(Article, lazy=True)
    customer = db.relationship(Person, lazy=True)
