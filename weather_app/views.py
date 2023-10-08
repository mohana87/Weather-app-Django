from django.shortcuts import render
import datetime
import requests

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'amsterdam'
    
    appid = 'c2850db76d96766a980c3b7f88d5b5f9'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city,"appid":appid , "units":'metric'}
    r = requests.get(url=URL,params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']    
    temp = res['main']['temp']
    
    day = datetime.date.today()
    
    return render(request,'index.html',{'description':description ,'icon':icon , 'temp': temp , 'day': day , 'city': city})