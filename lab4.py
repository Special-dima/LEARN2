from flask import Blueprint, render_template, request
lab4= Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/uspeh')
def uspeh():
    return render_template('uspeh.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    if username == '':
        error = 'Не введен логин'
        return render_template('login.html', error=error, username=username)
    password = request.form.get('password')
    if password == '':
        error = 'Не введен пароль'
        return render_template('login.html', error=error, password=password)
    
    if username == 'alex' and password == '123':
        return render_template('uspeh.html', username=username, password=password)
    else:
        error = 'Неверный логин и/или пароль'
        return render_template('login.html', error=error, username=username, password=password)
    

@lab4.route('/lab4/holod', methods=['GET', 'POST'])
def holod():
    if request.method == 'GET':
        return render_template('holod.html')
    
    temperature = request.form.get('temperature')
    error = ''
    message = ''  # Начальное значение для переменной message
    snowflakes = ''  # Начальное значение для переменной snowflakes
    
    if temperature is None or temperature == '':
        error = 'ошибка: не задана температура'
    elif int(temperature) < -12:#int(temperature) преобразует значение переменной temperature в целочисленный тип данных. 
        error = 'не удалось установить температуру — слишком низкое значение'
    elif int(temperature) > -1:
        error = 'не удалось установить температуру — слишком высокое значение'
    elif -12 <= int(temperature) <= -9:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️❄️❄️'
    elif -8 <= int(temperature) <= -5:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️❄️'
    elif -4 <= int(temperature) <= -1:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️'
    
    return render_template('holod.html', error=error, temperature=temperature, message=message, snowflakes=snowflakes)


@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template('zerno.html')

    error = ''
    zerno = request.form.get('zerno')
    ves = request.form.get('ves')
    message = ''

    if ves is None or ves == '':
        error = 'не введен вес'
    elif float(ves) <= 0: #float преобразует переданное ей значение в число с плавающей запятой
        error = 'неверное значение веса'
    elif zerno:
        if zerno == 'ячмень':
            price = 12000
        elif zerno == 'овес':
            price = 8500
        elif zerno == 'пшеница':
            price = 8700
        elif zerno == 'рожь':
            price = 14000

        total_cost = float(ves) * price

        if float(ves) > 50:
            total_cost *= 0.9
            message = 'Заказ успешно сформирован. Вы заказали {}. Вес: {} т. Сумма к оплате: {} руб. Применена скидка за большой объем.'.format(zerno, ves, total_cost)
        else:
            message = 'Заказ успешно сформирован. Вы заказали {}. Вес: {} т. Сумма к оплате: {} руб.'.format(zerno, ves, total_cost)

        if float(ves) > 500:
            message = 'Такого объема сейчас нет в наличии.'

    return render_template('zerno.html', error=error, zerno=zerno, ves=ves, message=message)


@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')

    color = request.form.get('color')
    backcolor = request.form.get('backcolor')
    font_size = request.form.get('font_size')
    if color == backcolor:
        # Если цвет текста совпадает с цветом фона
        error_msg = 'Цвет текста и фона одинаковые, выберите разные цвета'
        return render_template('error.html', error_msg=error_msg)
    headers = {
        'Set-Cookie': [
            'color=' + color + ' ; path=/',
            'backcolor=' + backcolor + ' ; path=/',
            'font_size=' + str(font_size) + ' ; path=/'
        ],
        'Location': '/lab4/cookies'
    }

    return '', 303, headers # возвращает кортеж, состоящий из трех элементов: пустой строки, числа 303 и переменной headers.
    #число 303 указывает на статус перенаправления (Redirect)
    