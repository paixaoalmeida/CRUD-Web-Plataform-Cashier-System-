from flask import Flask
from flask import render_template
from flask import url_for

web = Flask(__name__)


@web.route("/")
def hello():
    url_for('static', filename='style.css')
    return render_template('page.html')

