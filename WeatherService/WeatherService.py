import urllib2
import json
from DbHelper import DbHelper
def get_current_weather(city):
    city_geo = get_city_code(city)
    city_weather = 'http://api.wunderground.com/api/4488808ba46b3f41/conditions' + city_geo + '.json'
    print city_weather
    weather_stream = urllib2.urlopen(city_weather)
    city_weather_string = weather_stream.read()
    parsed_city_weather = json.loads(city_weather_string)
    print city_weather_string
    wind_mph = parsed_city_weather['current_observation']['wind_mph']
    print wind_mph
    return

def get_history_weather(city, date):
    city_geo = get_city_code(city)
    #weather_history_query_string = http://api.wunderground.com/api/4488808ba46b3f41/history_YYYYMMDD/q/CA/San_Francisco.json
    weather_history_query_string = 'http://api.wunderground.com/api/4488808ba46b3f41/history_' + date +city_geo+ '.json'
    print weather_history_query_string
    history_weather_stream = urllib2.urlopen(weather_history_query_string)
    city_history_weather_string = history_weather_stream.read()
    print city_history_weather_string
    parsed_history_weather = json.loads(city_history_weather_string)
    observations = parsed_history_weather['history']['observations']
    return

def get_forecast(city):
    #http://api.wunderground.com/api/4488808ba46b3f41/forecast/q/CA/San_Francisco.json
    city_geo = get_city_code(city)
    weather_forecast_query_string = 'http://api.wunderground.com/api/4488808ba46b3f41/forecast' + city_geo+ '.json'
    print weather_forecast_query_string
    forecast_weather_stream = urllib2.urlopen(weather_forecast_query_string)
    city_forecast_weather_string = forecast_weather_stream.read()
    print city_forecast_weather_string
    parsed_forecast_weather = json.loads(city_forecast_weather_string)
    #observations = parsed_history_weather['history']['observations']
    forecast = parsed_forecast_weather['forecast']['simpleforecast']['forecastday']
    return

def get_forecast10d(city):
    #http://api.wunderground.com/api/4488808ba46b3f41/forecast/q/CA/San_Francisco.json
    city_geo = get_city_code(city)
    weather_forecast_query_string = 'http://api.wunderground.com/api/4488808ba46b3f41/forecast10day' + city_geo+ '.json'
    print weather_forecast_query_string
    forecast_weather_stream = urllib2.urlopen(weather_forecast_query_string)
    city_forecast_weather_string = forecast_weather_stream.read()
    print city_forecast_weather_string
    parsed_forecast_weather = json.loads(city_forecast_weather_string)
    #observations = parsed_history_weather['history']['observations']
    forecasts = parsed_forecast_weather['forecast']['simpleforecast']['forecastday']
    forecast10days = []
    for forecastday in forecasts:
        dateyear = forecastday['date']['year']
        datemonth = forecastday['date']['month']
        dateday = forecastday['date']['day']
        low = forecastday['low']['celsius']
        high = forecastday['high']['celsius']
        maxwind = forecastday['maxwind']
        avewind = forecastday['avewind']
        forecast10days.append({'date':str(dateyear)+'/'+str(datemonth)+'/'+str(dateday),'low':low,'high':high,'maxwind':maxwind,'avewind':avewind})
    return forecast10days

def get_city_code(city):
    city_query_str = 'http://api.wunderground.com/api/4488808ba46b3f41/geolookup/q/China/' + city + '.json'
    print 'query city code string:' + city_query_str
    response_stream = urllib2.urlopen(city_query_str)
    city_json_string = response_stream.read()
    parsed_city_geo = json.loads(city_json_string)
    result = parsed_city_geo['response']['results']
    city_geo = result[1]['l']
    print city_geo
    return city_geo



if __name__ == "__main__":
    #get_history_weather('wuhan','20110909')
    #get_forecast10d('wuhan')
    #forecasts = get_forecast10d('wuhan')
    db_helper = DbHelper()
    db_helper.mssqlconn()
    db_helper.test()
    #for forecast in forecasts:
    #    db_helper.update_weather_forecast(forecast['date'],forecast['low'],forecast['high'],forecast['maxwind'],forecast['avewind'])