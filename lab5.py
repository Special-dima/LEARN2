from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, Blueprint, render_template, request, session
import psycopg2

lab5 =Blueprint('lab5',__name__)

def dBConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "pivovarova_alina_base",
        password = "12345",
        port = 5433
    )

    return conn;

def dBClose(cursor,connection):
    cursor.close()
    connection.close()


@lab5.route("/lab5/")
def main():
    visibleUser = session.get('username', 'Anon')
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="pivovarova_alina_base",
        password="12345",
        port = 5433
    )
    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()
    # Пишем запрос, который курсор должен выполнить
    cur.execute("SELECT * FROM users;")
    # fetchall - получить все строки, которые получились в результате выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    # Закрываем соединение с БД
    cur.close()
    conn.close()

    print(result)

    return render_template('lab5.html', username=visibleUser)


@lab5.route('/lab5/users')
def user():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "pivovarova_alina_base",
        password = "12345",
        port = 5433
    )
    cur = conn.cursor() #создает курсор, привязанный к соединению (conn), которое уже было установлено с базой данных 
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    return render_template('lab5users.html', users=result)
