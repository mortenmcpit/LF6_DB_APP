from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, FloatField, SubmitField, DateField
from wtforms.validators import Length, DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from DB_APP import db
from DB_APP.Main.utils import articlenumgenerator, customernumgenerator, producernumgenerator
from DB_APP.Main.models import Producer, Person, Order, Article


# Create new or Edit existing Articles
class ArticleForm(FlaskForm):
    producernumber = QuerySelectField(
        label="Hersteller",
        query_factory=lambda: Producer.query.all(),
        get_label="producername",
    )
    articlename = StringField()
    price = FloatField()

    def save(self):
        article = Article(
            articlenumber=articlenumgenerator(),
            producernumber=self.producernumber.data.producernumber,
            articlename=self.articlename.data,
            price=self.price.data)
        db.session.add(article)
        db.session.commit()

    def update(self, obj):
        pass

    def fill(self, obj):
        pass


# Create new or Edit existing Orders
class OrderForm(FlaskForm):
    ordernumber = IntegerField()
    articlenumber = QuerySelectField(
        label="Artikel",
        query_factory=lambda: Article.query.all(),
        get_label="articlename",
    )
    customernumber = QuerySelectField(
        label="Kunde",
        query_factory=lambda: Person.query.all(),
        get_label="Kundennummer",
    )
    articlequantity = IntegerField()
    ordersum = IntegerField()

    def save(self):
        order = Order(ordernumber=self.ordernumber.data,
                      articlenumber=self.articlenumber.data.articlenumber,
                      customernumber=self.customernumber.data.customernumber,
                      articlequantity=self.articlequantity.data,
                      ordersum=self.ordersum.data)
        db.session.add(order)
        db.session.commit()

    def update(self, obj):
        pass

    def fill(self, obj):
        pass


# Create new or Edit existing Producers
class ProducerForm(FlaskForm):
    producernumber = IntegerField()
    producername = StringField()
    country = StringField()

    def save(self):
        producer = Producer(producernumber=producernumgenerator(),
                            producername=self.producername.data,
                            country=self.country.data)
        db.session.add(producer)
        db.session.commit()

    def update(self, obj):
        pass

    def fill(self, obj):
        pass


# Create new or Edit existing Persons
class PersonForm(FlaskForm):
    # personnumber = IntegerField()
    lastname = StringField()
    firstname = StringField()
    street = StringField()
    place = StringField()
    zipcode = IntegerField()
    country = StringField()
    birthday = DateField()

    def save(self):
        person = Person(personnumber=customernumgenerator(),
                        lastname=self.lastname.data,
                        firstname=self.firstname.data,
                        street=self.street.data,
                        place=self.place.data,
                        country=self.country.data,
                        birthday=self.birthday.data,
                        zipcode=self.zipcode.data)
        db.session.add(person)
        db.session.commit()

    def update(self, obj):
        pass

    def fill(self, obj):
        pass
