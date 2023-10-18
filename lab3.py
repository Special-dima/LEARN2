from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    #Пусть кофе стоит 120 рублей, чёрный чай — 80 рублей, зелёный — 70 рублей
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
         price = 80
    else: 
        price = 70 
    #Добавка молока удорожает напиток на 30 рублей, а сахара — на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
        
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    familiya = request.args.get('familiya')
    if familiya == '':
        errors['familiya'] = 'Заполните поле!'

    name = request.args.get('name')
    if name == '':
        errors['name'] = 'Заполните поле!'

    otchestvo = request.args.get('otchestvo')
    if otchestvo == '':
        errors['otchestvo'] = 'Заполните поле!'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    start = request.args.get('start')
    if start == '':
        errors['start'] = 'Заполните поле!'

    finish = request.args.get('finish')
    if finish == '':
        errors['finish'] = 'Заполните поле!'

    data = request.args.get('data')
    if data == '':
        errors['data'] = 'Заполните поле!'

    bagaz = request.args.get('bagaz')

    tipe = request.args.get('tipe')

    polka = request.args.get('polka')

    return render_template('ticket.html', familiya=familiya, name=name, otchestvo=otchestvo, age=age, 
    start=start, finish=finish, data=data, bagaz=bagaz, tipe=tipe, polka=polka, errors=errors)


@lab3.route('/lab3/bilet')
def bilet():
    return render_template('bilet.html')