from flask import Blueprint, jsonify, request
from mysql import connector
import json


simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/news/<int:id>')
def get_news_id(id):
    connection=connector.connect(
        host = "localhost",
        user = "covid-19-user",
        password = "covid-19-pass",
        db = "CC_T3"
    )
    cursor = connection.cursor(prepared=True)
    try:
        print(id)
        cursor.execute("select * from News where News.ID = %s ", (int(id),))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(cursor.statement)
    cursor.close()
    connection.close()
    return response


@simple_page.route('/news/<string:title>')
def get_news_title(title):
    connection=connector.connect(
        host = "localhost",
        user = "covid-19-user",
        password = "covid-19-pass",
        db = "CC_T3"
    )
    cursor = connection.cursor()
    cursor.execute("select * from News where title = %s", (title,))
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response


@simple_page.route('/news', methods = ["GET", "POST"])
def push_news():
    if request.method == "GET":
        connection=connector.connect(
            host = "localhost",
            user = "covid-19-user",
            password = "covid-19-pass",
            db = "CC_T3"
        )
        cursor = connection.cursor()
        cursor.execute("select * from News")
        response = jsonify(cursor.fetchall())
        cursor.close()
        connection.close()
        return response

    if request.method == 'POST':
        connection=connector.connect(
            host = "localhost",
            user = "covid-19-user",
            password = "covid-19-pass",
            db = "CC_T3"
        )
        title = request.form['title']
        content = request.form['content']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into News (title, content) values (%s, %s)",(title, content))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status":"failure"})
            print(e)
        cursor.close()
        connection.close()
        return response