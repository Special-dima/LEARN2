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
            НГТУ, ФБ, WEB-программирование, часть 2. Спиок лабораторных
            </header>

            <ol>
             <a href="/lab1" target="_blank" >Первая лабораторная</a>
            </ol>
            <ol>
             <a href="/lab2" target="_blank" >Вторая лабораторная</a>
            </ol>
            <ol>
             <a href="/lab3/" target="_blank" >Третья лабораторная</a>
            </ol>

            <footer>
            &copy; Нехороших Дмитрий Алексеевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""


