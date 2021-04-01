from flask import Blueprint
simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/news')
def get_news():
    return "stiri"