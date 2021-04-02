from flask import Blueprint, jsonify, request
from mysql import connector


simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/hospital', methods = ["GET", "POST"])
def push_news():
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
        adress = request.form['adress']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Hospital (name, adress) values (%s, %s)",(name, adress))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status":"failure"})
            print(e)
        cursor.close()
        connection.close()
        return response

    @simple_page.route('/hospital/<string:name>')
    def get_news_title(name):
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