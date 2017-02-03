### About #####################################################################
#                                                                             #
# This code is part of the Simmons Hall Dashboard project. An up-to-date      #
# version can be found at https://github.com/simmons-tech/dashboard .         #
#                                                                             #
# The project is built an maintained by Simmons Tech, a student organization  #
# at MIT. The original code was produced by Luke O'Malley '14 and             #
# Will Oursler '15                                                            #
#                                                                             #
### License and Warranty ######################################################
#                                                                             #
# Copyright 2013 Simmons Hall                                                 #
#                                                                             #
# Licensed under LGPL3 (the "License"). You may not use this work except in   #
# compliance with the License. You may obtain a copy of the License at        #
# http://opensource.org/licenses/lgpl-3.0.html .                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.            #
###############################################################################

from django.http import HttpResponse
import pyowm
import json

def getWeather(request):
    try:
	print('Trying to get weather...')
        # Zip Code
        location_id = '02139'
        owm = pyowm.OWM("40964e665cd10d202b248a68c1b688fe")
	CITY_ID = 5111144
	current = owm.weather_at_id(CITY_ID)
	w = current.get_weather()
	fc = owm.daily_forecast_at_id(CITY_ID, limit=2)

	forecast_weather = [fo for fo in fc.get_forecast()]
	current_weather = w

        current = { 'temp': current_weather.get_temperature('fahrenheit')['temp'],
                    'description': current_weather.get_detailed_status(),
                    'icon': code2image(current_weather.get_weather_icon_name()),}
	
	w_today = forecast_weather[0]
	temp_today = w_today.get_temperature('fahrenheit')
        today = { 'high': temp_today['max'],
                  'low': temp_today['min'],
                  'description': w_today.get_detailed_status(),
                  'icon': code2image(w_today.get_weather_icon_name()),}

	
	w_tomorrow = forecast_weather[1]
	temp_tomorrow = w_tomorrow.get_temperature('fahrenheit')
        tomorrow = { 'high': temp_tomorrow['max'],
                  'low': temp_tomorrow['min'],
                  'description': w_tomorrow.get_detailed_status(),
                  'icon': code2image(w_tomorrow.get_weather_icon_name()),}

    except Exception as e:
	print('Exception: ', e)
        current = {'temp': 'NA',
                   'description': 'NA',
                   'icon': 'NA',}

        today = tomorrow = {'high': 'NA',
                            'low': 'NA',
                            'description': 'NA',
                            'icon': 'NA',}
    
    weather = { 'title': 'Yahoo! Weather',
                'current': current,
                'today': today,
                'tomorrow': tomorrow,}
    
    jsonout = json.dumps(weather)
    return HttpResponse(jsonout, content_type="application/json")

def code2image(code):
    weather = {
		'0':'windy.png',
		'1':'windy.png',
		'2':'windy.png',
		'11d':'thunder.png',
		'11n':'thunder.png',
		'5':'mixed.png',
		'6':'mixed.png',
		'7':'mixed.png',
		'8':'mixed.png',
		'10d':'rain.png',
                '10n':'rain.png',
		'10':'mixed.png',
		'11':'rain.png',
		'12':'rain.png',
		'Snow':'snow.png',
		'14':'snow.png',
		'15':'snow.png',
		'16':'snow.png',
		'50d':'mixed.png',
		'50n':'mixed.png',
		'19':'foggy.png',
		'20':'foggy.png',
		'21':'foggy.png',
		'22':'foggy.png',
		'23':'windy.png',
		'24':'windy.png',
		'25':'cold.png',
		'04d':'cloudy.png',
		'04n':'cloudy.png',
		'03d':'cloudy.png',
		'03n':'cloudy.png',
		'02n':'patchy_night.png',
		'02d':'patchy.png',
		'01n':'clear_night.png',
		'01d':'sunny.png',
		'33':'clear_night.png',
		'34':'sunny.png',
		'35':'mixed.png',
		'36':'hot.png',
		'11d':'thunder.png',
		'11n':'thunder.png',
		'39':'thunder.png',
		'40':'rain.png',
		'13d':'snow.png',
		'13n':'snow.png',
		'43':'snow.png',
		'44':'patchy.png',
		'45':'thunder.png',
		'46':'snow.png',
		'47':'thunder.png',
		'3200':'no_icon.png'
	}

    # path that browser will use to find weather images
    image_path = "/static/img/"
    
    return "{}{}".format(image_path, weather[ code ])
