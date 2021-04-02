from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection


simple_page_4 = Blueprint('simple_page_4', __name__, template_folder='templates')


@simple_page_4.route('/vaccination_appointment', methods = ["GET", "POST"])
def vaccination_appointment():
    if request.method == "GET":
        connection=get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Vaccination_Appointment")
            response = jsonify(cursor.fetchall())
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
        cursor.close()
        connection.close()
        return response

    if request.method == 'POST':
        connection=get_db_connection()
        person_name = request.form['person_name']
        app_date = request.form['app_date']
        vacc_centre_ID = request.form['vacc_centre_ID']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Vaccination_Appointment (person_name, app_date, vacc_centre_ID) values (%s, %s, %s)",(person_name, app_date, vacc_centre_ID))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status":"failure"})
            print(e)
        cursor.close()
        connection.close()
        return response


@simple_page_4.route('/vaccination_appointment/<string:person_name>')
def get_vaccination_appontment_name(person_name):
    connection=get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Vaccination_Appointment where person_name = %s", (person_name,))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response