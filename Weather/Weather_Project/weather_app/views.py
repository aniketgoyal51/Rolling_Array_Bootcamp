from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if(request.method=='POST'):
        api_key='0c0404825022be0d52b563e044d5673d'
        location=request.POST['location']
        all_data=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ location +'&appid=' + api_key).read()
        json_data=json.loads(all_data)
        data={
            "location":str(json_data['name']),
            'Country_code':str(json_data['sys']['country']),
            "Coordinate":str(json_data["coord"]["lon"]) + " " + str(json_data['coord']['lat']),
            "Temp":str(json_data["main"]["temp"]), 
            "Pressure":str(json_data["main"]["pressure"]), 
            "Humidity":str(json_data["main"]["humidity"]),
        }
        print(json_data)
        return render(request,'index.html',{'data':data})
    else:
        return render(request,'index.html')


# {
#     'coord': {'lon': -0.1257, 'lat': 51.5085}, 
#     'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
#     'base': 'stations', 
#     'main': {'temp': 282.53, 'feels_like': 281.9, 'temp_min': 282.53, 'temp_max': 282.53, 'pressure': 996, 'humidity': 90, 'sea_level': 996, 'grnd_level': 990}, 
#     'visibility': 6140, 
#     'wind': {'speed': 1.69, 'deg': 94, 'gust': 3.17}, 
#     'clouds': {'all': 100}, 
#     'dt': 1744693877, 
#     'sys': {'country': 'GB', 'sunrise': 1744693463, 'sunset': 1744743372}, 
#     'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200
# }