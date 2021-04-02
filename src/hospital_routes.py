from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection


simple_page_2 = Blueprint('simple_page_2', __name__, template_folder='templates')


@simple_page_2.route('/hospital', methods = ["GET", "POST"])
def hospital():
    if request.method == "GET":
        connection=get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Hospital")
            response = jsonify(cursor.fetchall())
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
        cursor.close()
        connection.close()
        return response

    if request.method == 'POST':
        connection=get_db_connection()
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
    connection=get_db_connection()
    cursor = connection.cursor()
    cursor.execute("select * from Hospital where name = %s", (name,))
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response


@simple_page_2.route('/hospital/<int:id>')
def get_hospial_id(id):
    connection=get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from Hospital where Hospital.ID = %s ", (int(id),))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response