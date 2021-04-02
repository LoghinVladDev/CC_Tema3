from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection


simple_page_5 = Blueprint('simple_page_5', __name__, template_folder='templates')


@simple_page_5.route('/hospital_admission', methods = ["GET", "POST"])
def hospital_admission():
    if request.method == "GET":
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Hospital_Admission")
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
            request.form['admitted'], request.form['vaccinated'],
            request.form['hospital_ID'], request.form['entry_date'])
            cursor.execute(
                "insert into Hospital_Admission (admitted, vaccinated, hospital_ID, entry_date) values (%s, "
                "%s, %s, %s)", query_params)
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status": "failure", 'msg': str(e)})
            print(e)
        cursor.close()
        connection.close()
        return response


@simple_page_5.route('/hospital_admission/<string:entry_date>')
def get_hospital_admission_date(entry_date):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Hospital_Admission where entry_date = %s", (entry_date,))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page_5.route('/hospital_admission/<int:id>')
def get_hospial_admission_id(id):
    connection=get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from Hospital_Admission where hospital_ID = %s ", (int(id),))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response