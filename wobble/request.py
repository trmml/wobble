from english import English
import requests

class Request():
	def __init__(self):
		self.api_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_%s.geojson'
		self.url = { 'main': self.api_url % 'hour', 'test': self.api_url % 'month' }

	def get(self):
		r = requests.get(self.url['main']) # main/test for dev purposes
		if r.status_code == 200:
			if len(r.json()['features']) > 0:
				earthquake = English(r.json())
				return {'sentence': earthquake.sentence(), 'url': earthquake.url(), 'is_quake': True }
			else:
				return { 'sentence': 'No Recent Significant Earthquakes', 'is_quake': False}
		else:
			return "Error: Status code {}".format(r.status_code)
