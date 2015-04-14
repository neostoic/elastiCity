# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import urllib
import pprint

def get_city_attractions(topic_id):
    service_url = 'https://www.googleapis.com/freebase/v1/topic'
    params = {
      'filter': '/location/location'
    }
    url = service_url + topic_id + '?' + urllib.urlencode(params)
    topic = json.loads(urllib.urlopen(url).read())
    return topic
    # Eden, please note that if you need the attractions, call: get_city_attractions(topic_id)['property']['/location/location/contains']
    # geo info, get_city_attractions(topic_id)['/location/location/geolocation']
if __name__ == '__main__':
    city_id = '/m/04jpl' # topic id of London for example
    pprint.pprint(get_city_attractions(city_id)['property']['/location/location/contains'])