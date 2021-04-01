from src.news_routes import simple_page
from flask import Flask

app = Flask(__name__)
app.register_blueprint(simple_page)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    app.register_blueprint(simple_page)
