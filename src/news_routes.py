from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection
from src.translation_api import translate_text


simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/news/<int:id>')
def get_news_id(id):
    connection = get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from News where News.ID = %s ", (int(id),))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page.route('/news/<string:title>')
def get_news_title(title):
    connection=get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("select * from News where title = %s", (title,))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page.route('/news/<string:title>/translate/<string:language>')
def get_news_title_translated(title, language):
    connection=get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("select * from News where title = %s", (title,))
        response = jsonify(translate_text(language, str(cursor.fetchall())))
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page.route('/translate', methods=["POST"])
def translate():
     language = request.form['language']
     input_text = request.form['text']
     return translate_text(language, input_text)


@simple_page.route('/news', methods = ["GET", "POST"])
def news():
    if request.method == "GET":
        connection=get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from News")
            response = jsonify(cursor.fetchall())
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
        cursor.close()
        connection.close()
        return response

    if request.method == 'POST':
        connection=get_db_connection()
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

