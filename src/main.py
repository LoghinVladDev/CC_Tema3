from src.news_routes import simple_page
from src.hospital_routes import simple_page_2
from src.vaccination_centre_routes import simple_page_3
from src.vaccination_appointment_routes import simple_page_4
from flask import Flask

app = Flask(__name__)
app.register_blueprint(simple_page)
app.register_blueprint(simple_page_2)
app.register_blueprint(simple_page_3)
app.register_blueprint(simple_page_4)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    app.register_blueprint(simple_page)
    app.register_blueprint(simple_page_2)
    app.register_blueprint(simple_page_3)
    app.register_blueprint(simple_page_4)
