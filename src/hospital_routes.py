from flask import Blueprint, jsonify, request
from mysql import connector


simple_page_2 = Blueprint('simple_page_2', __name__, template_folder='templates')


@simple_page_2.route('/hospital', methods = ["GET", "POST"])
def hospital():
    if request.method == "GET":
        connection=connector.connect(
            host = "localhost",
            user = "covid-19-user",
            password = "covid-19-pass",
            db = "CC_T3"
        )
        cursor = connection.cursor()
        cursor.execute("select * from Hospital")
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
        name = request.form['name']
        address = request.form['address']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Hospital (name, address) values (%s, %s)",(name, address))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status":"failure"})
            print(e)
        cursor.close()
        connection.close()
        return response


@simple_page_2.route('/hospital/<string:name>')
def get_hospital_name(name):
    connection = connector.connect(
        host="localhost",
        user="covid-19-user",
        password="covid-19-pass",
        db="CC_T3"
    )
    cursor = connection.cursor()
    cursor.execute("select * from News where title = %s", (name,))
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response