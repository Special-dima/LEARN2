from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>Нехороших Дмитрий Алексеевич, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Нехороших Дмитрий Алексеевич, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
     <head>
           <title>Нехороших Дмитрий Алексеевич, лабораторная 1</title>
     </head>
     <body>
            <header>
            НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>
            <p>
            Flask - фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </p>
            <a href="/menu" target="_blank" >Меню</a>
            <h2>Реализованные роуты</h2>
            <ul>
                <li>
                    <a href="/lab1/oak" target="_blank" >/lab1/oak - дуб</a>
                </li>
                <li>
                    <a href="/lab1/student" target="_blank" >/lab1/student - студент</a>
                </li>
                <li>
                <a href="/lab1/python" target="_blank" >/lab1/python - python</a>
                </li>
                <li>
                    <a href="/lab1/lika" target="_blank" >/lab1/lika - Лика</a>
                </li>
            </ul>

            <footer>
            &copy; Нехороших Д.А., ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return'''
<!doctype html>
<html>
     <head>
        <title>Нехороших Дмитрий Алексеевич, лабораторная 1</title>
    </head>
     <body>
     <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <h1>Дуб</h1>
          <img src=''' + url_for('static', filename='oak.jpg') + '''>
    <footer>
    &copy; Нехорошмх Д.А., ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
@app.route('/lab1/student')
def student():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Нехороших Дмитрий Алексеевич, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>

          <h1>Нехороших Дмитрий Алексеевич</h1>

          <img src=''' + url_for('static', filename='logo.jpg') + '''>
    <footer>
    &copy; Нехороших Д.А., ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Нехороших Дмитрий Алексеевич, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>

          <p>Python, согласно данным из Google – язык программирования высокого уровня общего назначения.
          Обладает типизацией динамического строгого характера. Имеет автоматическое управление памятью, за счет чего осуществляется
          повышение производительности контента, написанного на нем.</p>
          
          <p>Python – объектно-ориентированный язык программирования, пользующийся спросом у большинства
          современных разработчиков. Коды, написанные на нем, достаточно легко читать.</p>
          
          <p>Python - это простой в освоении, но мощный и универсальный язык сценариев,
          что делает его привлекательным для разработки приложений.</p>

          <img src=''' + url_for('static', filename='python.jpg') + '''>
    <footer>
    &copy; Нехороших Д.А., ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
@app.route('/lab1/lika')
def knopka():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Нехороших Дмитрий Алексеевич, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>

          <p>В нашей семье есть собака по имени Кнопка. Она очень любит покушать, поэтому у нее образовалось пузико.
          Но оно не мешает ей бегать по улице и нюхать цветочки!</p>
          
          <p>У нашей собаки есть личные границы, поэтому, когда мы приходим к ней играть во время ее сна или не очень хорошего настроения,
          то можем поолучить в ответ агрессивный рык. Но она все равно нас очень любит, просто нас много, а она одна. Пёселям
          тоже надо отдыхать!</p>
          
          <p>Кнопке очень не нравятся мои тапки с помпонами, поэтому при их виде она начинает грызть мои тапочки. Еще у нее есть расписание:
          в восемь утра она готова принимать вкусняшки на завтрак, потом она спит до десяти, после этого идет гулять. Далее
          в течение всего дня она не упускает возможность выпросить вкусняшку и поспать, а вечером она идет на проверку своей территории. В 
          девять вечера она уже готова ко сну и не желает никого видеть.</p>

          <img src=''' + url_for('static', filename='lika.jpg') + '''>
    <footer>
    &copy; Нехороших Д.А., ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
@app.route('/lab2/example')
def example():
    name = 'Нехороших дмитрий'
    laba2 = 'Лабораторная работа 2'
    group = 'ФБИ-14'
    kurs = '3 курс'
    student = 'Пивоварова Алина.'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши',  'price': 120},
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
        ]
    books = [
        {'author': 'Толстой Л.Н.', 'nazv': 'Анна Каренина', 'zanr': 'Классика', 'str': '159 страниц'},
        {'author': 'Джейн Остин', 'nazv': 'Гордость и предубеждение', 'zanr': 'Классика', 'str': '423 страницы'},
        {'author': 'Патрик Ленсиони', 'nazv': 'Евгений Онегин', 'zanr': 'Классика', 'str': '542 страницы'},
        {'author': 'Джек Лондон', 'nazv': 'Мартин Иден', 'zanr': 'Классика', 'str': '600 страниц'},
        {'author': 'Уильям Шекспир', 'nazv': 'Ромео и джульетта', 'zanr': 'Классика', 'str': '450 страниц'},
        {'author': 'Станислав Лем', 'nazv': 'Солярис', 'zanr': 'Фантастика', 'str': '320 страниц'},
        {'author': 'Фрэнк Герберт', 'nazv': 'Дюна', 'zanr': 'Фантастика', 'str': '400 страниц'},
        {'author': 'Дэн Симмонс', 'nazv': 'Гиперион', 'zanr': 'Фантастика', 'str': '243 страницы'},
        {'author': 'Нил Стивенсон', 'nazv': 'Анафем', 'zanr': 'Фантастика', 'str': '156 страниц'},
        {'author': 'Айзек Азимов', 'nazv': 'Конец вечности', 'zanr': 'Фантастика', 'str': '356 страниц'}
        ]
    return render_template('example.html', 
                            name=name, laba2=laba2, group=group,
                            kurs=kurs, student=student, fruits=fruits, books=books)
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/cake')
def cake():
    return render_template('cake.html')