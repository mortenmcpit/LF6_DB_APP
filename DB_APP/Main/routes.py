from flask import Blueprint, render_template, request, redirect, url_for, flash
from DB_APP.Main.utils import articlenumgenerator
from DB_APP.Main.models import *
from DB_APP.Main.forms import ArticleForm, PersonForm, OrderForm, ProducerForm

main = Blueprint('main', __name__)
""" Pages """
"""Home Page"""


@main.route('/', methods=['GET', 'POST'])
def homepage():
    number = articlenumgenerator()

    persons = Person.query.all()
    orders = Order.query.all()
    return render_template('pages/homepage.html', persons=persons, orders=orders, number=number)


""" Articles Page """


@main.route('/articles', methods=['GET', 'POST'])
def articles():
    articles = Article.query.all()
    return render_template('pages/articles.html', articles=articles)


""" Producers Page """


@main.route('/producers', methods=['GET', 'POST'])
def producers():
    producers = Producer.query.all()
    return render_template('pages/producers.html', producers=producers)


""" Customer Page """


@main.route('/customers', methods=['GET', 'POST'])
def customers():
    customers = Person.query.all()
    return render_template('pages/customers.html', customers=customers)


""" Form Routes """


@main.route('/add_article', methods=['GET', 'POST'])
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('Neuer Artikel hinzugefügt')
        return redirect(url_for('main.homepage'))
    return render_template('pages/add_article.html', form=form)


@main.route('/add_order', methods=['GET', 'POST'])
def add_order():
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('Bestellung abgeschickt')
        return redirect(url_for('main.homepage'))
    return render_template('', form=form)


@main.route('/add_producer', methods=['GET', 'POST'])
def add_producer():
    form = ProducerForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('neuer Hersteller eingetragen')
        return redirect(url_for('main.homepage'))
    return render_template('pages/add_producer.html', form=form)


@main.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = PersonForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('neuer Kunde eingetragen')
        return redirect(url_for('main.homepage'))
    return render_template('pages/add_customer.html', form=form)
