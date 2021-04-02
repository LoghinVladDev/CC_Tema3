from flask import Blueprint, jsonify, request

from src.dbconn import get_db_connection

simple_page_2 = Blueprint('simple_page_2', __name__, template_folder='templates')


@simple_page_2.route('/hospital', methods=["GET", "POST"])
def hospital():
    if request.method == "GET":
        connection = get_db_connection()
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
        connection = get_db_connection()
        name = request.form['name']
        address = request.form['address']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Hospital (name, address) values (%s, %s)", (name, address))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
        cursor.close()
        connection.close()
        return response


@simple_page_2.route('/hospital/<string:name>')
def get_hospital_name(name):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("select * from Hospital where name = %s", (name,))
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response


@simple_page_2.route('/hospitalopinion/', methods=['GET'])
def get_hospital_opinions():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Hospital_Opinion')
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response


@simple_page_2.route('/hospitaladmisssion/', methods=['GET'])
def get_hospital_opinions():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Hospital_Admission')
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response


@simple_page_2.route('/hospital', methods=['POST'])
def post_hospital():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query_params = (request.form['name'], request.form['address'])
        cursor.execute("insert into Hospital (name, address) values (%s, %s)", query_params)
        connection.commit()
        response = jsonify({"status": "success"})
    except Exception as e:
        response = jsonify({"status": "failure", 'msg': str(e)})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page_2.route('/hospitalopinion/', methods=['POST'])
def post_hospital():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query_params = (request.form['title'], request.form['message'], request.form['hospital_ID'])
        cursor.execute("insert into Hospital_Opinion (title, message, hospital_ID) values (%s, %s, %s)", query_params)
        connection.commit()
        response = jsonify({"status": "success"})
    except Exception as e:
        response = jsonify({"status": "failure", 'msg': str(e)})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page_2.route('/hospitaladmission/', methods=['POST'])
def post_hospital():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query_params = (request.form['admitted'], request.form['vaccinated'],
                        request.form['hospital_ID'], request.form['entry_date'])
        cursor.execute("insert into Hospital_Admission (admitted, vaccinated, hospital_ID, entry_date) values (%s, "
                       "%s, %s, %s)", query_params)
        connection.commit()
        response = jsonify({"status": "success"})
    except Exception as e:
        response = jsonify({"status": "failure", 'msg': str(e)})
        print(e)
    cursor.close()
    connection.close()
    return response



