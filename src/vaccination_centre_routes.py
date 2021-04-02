from flask import Blueprint, jsonify, request
from mysql import connector


simple_page_3 = Blueprint('simple_page_2', __name__, template_folder='templates')

@simple_page_2.route('/vaccination_centre', methods = ["GET", "POST"])
def hospital():
    if request.method == "GET":
        connection=connector.connect(
            host = "localhost",
            user = "covid-19-user",
            password = "covid-19-pass",
            db = "CC_T3"
        )
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Vaccination_Centre")
            response = jsonify(cursor.fetchall())
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
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
        address = request.form['address']
        dose_count = request.form['dose_count']
        dose_type_ID = request.form['name']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Vaccination_Centre (address, dose_count, dose_type_ID) values (%s, %s)",(name, address))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status":"failure"})
            print(e)
        cursor.close()
        connection.close()
        return response