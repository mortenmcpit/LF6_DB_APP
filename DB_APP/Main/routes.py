from flask import Blueprint, render_template, request, redirect, url_for, flash
from DB_APP.Main.models import *
from DB_APP.Main.forms import ArticleForm, PersonForm, OrderForm, ProducerForm

main = Blueprint('main', __name__)
""" Pages """
"""Home Page"""


@main.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('pages/homepage.html')


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
    form = PersonForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('neuer Kunde eingetragen', 'success')
        return redirect(url_for('main.customers'))
    return render_template('pages/customers.html', customers=customers, form=form)


""" Orders Page """


@main.route('/orders', methods=['GET', 'POST'])
def orders():
    orders = Order.query.all()
    return render_template('pages/orders.html', orders=orders)


""" Form Routes """
""" Add """


@main.route('/add_article', methods=['GET', 'POST'])
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('Neuer Artikel hinzugefügt', 'success')
        return redirect(url_for('main.articles'))
    return render_template('pages/article_form.html', form=form)


@main.route('/add_order', methods=['GET', 'POST'])
def add_order():
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('Bestellung abgeschickt', 'success')
        return redirect(url_for('main.orders'))
    return render_template('pages/order_form.html', form=form)


@main.route('/add_producer', methods=['GET', 'POST'])
def add_producer():
    form = ProducerForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('neuer Hersteller eingetragen', 'success')
        return redirect(url_for('main.producers'))
    return render_template('pages/producer_form.html', form=form)


@main.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = PersonForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        flash('neuer Kunde eingetragen', 'success')
        return redirect(url_for('main.customers'))
    return render_template('pages/customer_form.html', form=form)


""" Edit """


@main.route('/edit_article/<int:id>', methods=['GET', 'POST'])
def edit_article(id):
    article = Article.query.get_or_404(id)
    form = ArticleForm(obj=article)
    if request.method == 'POST' and form.validate():
        form.update(obj=article)
        flash('Der Artikel wurde bearbeitet', 'success')
        return redirect(url_for('main.articles'))
    if request.method == "GET":
        form.fill(obj=article)
    return render_template('pages/article_form.html', form=form)


@main.route('/edit_producer/<int:id>', methods=['GET', 'POST'])
def edit_producer(id):
    producer = Producer.query.get_or_404(id)
    form = ProducerForm(obj=producer)
    if request.method == 'POST' and form.validate():
        form.update(obj=producer)
        flash('Der Hersteller wurde bearbeitet', 'success')
        return redirect(url_for('main.producers'))
    if request.method == "GET":
        form.fill(obj=producer)
    return render_template('pages/producer_form.html', form=form)


@main.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = Person.query.get_or_404(id)
    form = PersonForm(obj=customer)
    if request.method == 'POST' and form.validate():
        form.update(obj=customer)
        flash('Der Kunde wurde bearbeitet', 'success')
        return redirect(url_for('main.customers'))
    if request.method == "GET":
        form.fill(obj=customer)
    return render_template('pages/customer_form.html', form=form)


@main.route('/edit_order/<int:id>', methods=['GET', 'POST'])
def edit_order(id):
    order = Order.query.get_or_404(id)
    form = OrderForm(obj=order)
    if request.method == 'POST' and form.validate():
        form.update(obj=order)
        flash('Die Bestellung wurde bearbeitet', 'success')
        return redirect(url_for('main.orders'))
    if request.method == "GET":
        form.fill(obj=order)
    return render_template('pages/order_form.html', form=form)


""" Delete """


@main.route('/delete_article/<int:id>', methods=['GET', 'POST'])
def delete_article(id):
    article = Article.query.get_or_404(id)
    # form = request.form
    if request.method == 'POST':
        db.session.delete(article)
        db.session.commit()
        flash('Der Artikel wurde gelöscht', 'success')
        return redirect(url_for('main.articles'))
    # return render_template('pages/articles.html', article=article)


@main.route('/delete_order/<int:id>', methods=['GET', 'POST'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    # form = request.form
    if request.method == 'POST':
        db.session.delete(order)
        db.session.commit()
        flash('Die Bestellung wurde gelöscht', 'success')
        return redirect(url_for('main.orders'))
    return render_template('', order=order)


@main.route('/delete_producer/<int:id>', methods=['GET', 'POST'])
def delete_producer(id):
    producer = Producer.query.get_or_404(id)
    # form = request.form
    if request.method == 'POST':
        db.session.delete(producer)
        db.session.commit()
        flash('Der Hersteller wurde gelöscht', 'success')
        return redirect(url_for('main.producers'))
    return render_template('', producer=producer)


@main.route('/delete_customer/<int:id>', methods=['GET', 'POST'])
def delete_customer(id):
    customer = Person.query.get_or_404(id)
    # form = request.form
    if request.method == 'POST':
        db.session.delete(customer)
        db.session.commit()
        flash('Der Kunde wurde gelöscht', 'success')
        return redirect(url_for('main.customers'))
    return render_template('', customer=customer)

@main.route('/customer_orders/<int:id>', methods=['GET', 'POST'])
def customer_orders(id):
    customer = Person.query.get_or_404(id)
    orders = Order.query.filter_by(customernumber=id)
    return render_template('pages/costumer_orders.html', customer=customer, orders=orders)