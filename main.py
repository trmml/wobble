from flask import Flask, render_template, url_for, jsonify
from flask.ext.cors import CORS
from wobble.request import Request
import requests

app = Flask(__name__)
CORS(app)

earthquake = Request()
sentence = earthquake.get()['sentence']

@app.route('/')
def index():
    if earthquake.get()['is_quake']:
        colour = 'red'
    else:
        colour = 'blue'

    if colour == 'blue':
        title = sentence
    else:
        title = 'Recent Earthquake'

    favicon = url_for('static', filename=colour + '_favicon.ico') # dynamic favicons!

    return render_template('index.html', message=sentence, colour=colour, favicon=favicon, title=title)

@app.route('/api/earthquakes')
def earthquakes():
    data = { 'response': sentence, 'success': True }
    if earthquake.get()['is_quake']:
        data['url'] = earthquake.get()['url']

    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
