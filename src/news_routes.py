from flask import Blueprint, jsonify, request

from src import translation_api, sentiment_api, text_to_speech_api
from src.dbconn import get_db_connection


simple_page = Blueprint('simple_page', __name__, template_folder='templates')
simple_page8 = Blueprint('simple_page8', __name__, template_folder='templates')


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


@simple_page.route('/news/<int:id>/translate/<string:language>')
def get_news_id_translated(id, language):
    connection=get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("select * from News where ID = %s", (id,))
        response = jsonify(translate_text(language, str(cursor.fetchall()).replace("'", "")))
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response




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


@simple_page.route('/translate', methods=["POST"])
def translate():
    language = request.form['language']
    input_text = request.form['text']
    return translation_api.translate_text(language, input_text)


@simple_page.route('/sentiment', methods=["POST"])
def get_sentiment():
    input_text = request.form['text']
    analysis = sentiment_api.analyze(input_text)
    return jsonify(analysis)


@simple_page.route('/texttospeech', methods=["POST"])
def texttospeech():
    try:
        input_text = request.form['text']
        file_name = request.form['filename']
        audio_binary = text_to_speech_api.get_text_as_speech_binary(input_text, 'output')
        response = jsonify({"status": "success"})
    except Exception as e:
        response = jsonify({"status": "failure", 'message': str(e)})
    return response

