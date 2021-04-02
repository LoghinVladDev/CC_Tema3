from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection


simple_page_7 = Blueprint('simple_page_7', __name__, template_folder='templates')


@simple_page_7.route('/vaccine_type', methods = ["GET", "POST"])
def hospital_admission():
    if request.method == "GET":
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Vaccine_Type")
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
        name = request.form['name']
        try:
            cursor.execute(
                "insert into Hospital_Opinion (name) values (%s))", (name,))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status": "failure", 'msg': str(e)})
            print(e)
        cursor.close()
        connection.close()
        return response