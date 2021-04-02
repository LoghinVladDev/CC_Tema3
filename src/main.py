from src.news_routes import simple_page
from src.hospital_routes import simple_page_2
from src.vaccination_appointment_routes import simple_page_4
from src.hospital_admission_routes import simple_page_5
from src.hospital_opinion_routes import simple_page_6
from src.vaccine_type_routes import simple_page_7
from flask import Flask

app = Flask(__name__)
app.register_blueprint(simple_page)
app.register_blueprint(simple_page_2)
app.register_blueprint(simple_page_4)
app.register_blueprint(simple_page_5)
app.register_blueprint(simple_page_6)
app.register_blueprint(simple_page_7)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ciao')
def hey():
    return 'jajaj'


if __name__ == '__main__':
    app.run(debug=True)
    # app.register_blueprint(simple_page)
    app.register_blueprint(simple_page_2)
    app.register_blueprint(simple_page_3)
    app.register_blueprint(simple_page_4)
    app.register_blueprint(simple_page_5)
    app.register_blueprint(simple_page_6)
    app.register_blueprint(simple_page_7)
