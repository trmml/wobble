# -*- coding: utf-8 -*-
"""
Parses input into native, aesthetically pleasing English
Example of tweet style at twitter.com/WAGGNews/status/633736182782758913
"""

import datetime, re

# Braerules
# Numbers < 10 to be spelled out
# Distance measurement spelled out
class English():
    def __init__(self, input):
        self.input = input
        self.properties = self.input['features'][0]['properties']

    def raw(self): return self.input
    def magnitude(self): return self.properties['mag']
    def url(self): return self.properties['url']

    def place(self):
        def replace(match):
            d = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                '8': 'eight', '9': 'nine', 'N': 'North', 'E': 'East', 'S': 'South', 'W': 'West'}
            source = match.group(1).strip()

            if 'km' in source:
                source = source.split("km")[0].strip()
                return "{} kilometre{}".format(d.get(source, source), '' if source == '1' else 's')
            else:
                return d.get(source, source) + ' '

        return re.sub(r'(\d+ *km|[NESW]\s+(?=of))', replace, self.properties['place'])

    def time(self):
        timestamp = self.properties['time']
        value = datetime.datetime.fromtimestamp(timestamp/1000)
        return value.strftime("%H:%M")

    def sentence(self):
        values = { "magnitude":self.magnitude(), "place":self.place(), "time":self.time() }
        sentence = "Magnitude {magnitude} earthquake hits {place} at {time} UTC.".format(**values)
        return sentence.replace('–', '-')
