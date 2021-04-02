from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection
from src.translation_api import translate_text

simple_page_6 = Blueprint('simple_page_6', __name__, template_folder='templates')

@simple_page_6.route('/hospital_opinion', methods = ["GET", "POST"])
def hospital_admission():
    if request.method == "GET":
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Hospital_Opinion")
            response = jsonify(cursor.fetchall())
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
        cursor.close()
        connection.close()
        return response

    if request.method == 'POST':
        connection=get_db_connection()
        cursor = connection.cursor()
        try:
            query_params = (
            request.form['title'], request.form['message'],
            request.form['hospital_ID'])
            cursor.execute(
                "insert into Hospital_Opinion (title, message, hospital_ID) values (%s, "
                "%s, %s)", query_params)
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status": "failure", 'msg': str(e)})
            print(e)
        cursor.close()
        connection.close()
        return response


@simple_page_6.route('/hospital_opinion/<string:title>')
def get_hospital_opinion_title(title):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Hospital_Opinion where title = %s", (title,))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page_6.route('/hospital_opinion/<int:id>')
def get_hospial_admission_id(id):
    connection=get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from Hospital_Opinion where hospital_ID = %s ", (int(id),))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page_6.route('/hospital_opinion/<int:id>/translate/<string:language>')
def get_hospial_admission_id_translated(id, language):
    connection=get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from Hospital_Opinion where hospital_ID = %s ", (int(id),))
        response = jsonify(translate_text(language, str(cursor.fetchall()).replace("'", "")))
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response