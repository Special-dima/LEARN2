from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)

@lab1.route("/menu")
def menu():
    return"""
<!doctype html>
<html>
     <head>
           <title>НГТУ, ФБ, Лабораторные работы</title>
     </head>
     <body>
            <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Спиcок лабораторных
            </header>

            <ol>
             <a href="/lab1" target="_blank" >1)Лабораторная 1</a>
            </ol>
            <ol>
             <a href="/lab2/" target="_blank" >2)Лабораторная 2</a>
            </ol>
            <ol>
             <a href="/lab3/" target="_blank" >3)Лабораторная 3</a>
            </ol>
             <ol>
             <a href="/lab4/" target="_blank" >4)Лабораторная 4</a>
            </ol>
             <ol>
             <a href="/lab5/" target="_blank" >5)Лабораторная 5</a>
            </ol>
             <ol>
             <a href="/lab6/" target="_blank" >6)Лабораторная 6</a>
            </ol>
            <ol>
             <a href="/lab7/" target="_blank" >7)Лабораторная 7</a>
            </ol>
            <ol>
             <a href="/lab8/" target="_blank" >8)Лабораторная 8</a>
            </ol>
            <ol>
             <a href="/lab9/" target="_blank" >9)Лабораторная 9</a>
            </ol>

            <footer>
            &copy; Нехороших Дмитрий, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""

@lab1.route("/lab1")
def lab():
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
@lab1.route('/lab1/oak')
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
@lab1.route('/lab1/student')
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
@lab1.route('/lab1/python')
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
@lab1.route('/lab1/lika')
def lika():
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