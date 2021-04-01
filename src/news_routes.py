from flask import Blueprint, jsonify
from mysql import connector
import json


simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/news')
def get_news():
    connection=connector.connect(
        host = "localhost",
        user = "covid-19-user",
        password = "covid-19-pass",
        db = "CC_T3"
    )
    cursor = connection.cursor()
    cursor.execute("select * from Vaccine_Type")
    #return json.loads(str(cursor.fetchall()))
    response = jsonify(cursor.fetchall())
    cursor.close()
    connection.close()
    return response