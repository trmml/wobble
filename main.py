from flask import Flask, render_template, url_for, jsonify
from flask.ext.cors import CORS
from wobble.request import Request
import requests

app = Flask(__name__)
CORS(app)
earthquake = Request()

@app.route('/')
def index():
    skel = url_for('static', filename='bower_components/skeleton/css/skeleton.css')
    normalize = url_for('static', filename='bower_components/skeleton/css/normalize.css')
    css = url_for('static', filename='css/style.css')
    print
    print earthquake.get()
    print
    return render_template('index.html', normalize=normalize, skel=skel, css=css, earthquake=earthquake.get())

@app.route('/api/earthquakes')
def earthquakes():
	return jsonify(response=earthquake.get())

@app.errorhandler(404)
def page_not_found(e):
	return jsonify(error=404), 404

if __name__ == '__main__':
    app.run(debug=True)
