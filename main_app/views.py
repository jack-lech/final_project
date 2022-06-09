from multiprocessing import context
from django.shortcuts import render, redirect
import requests
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Comment
from django.views import generic


# Create your views here.
def main(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def webapp(request):
    city_list = [ "SanDiego", "Temecula", "Murrieta", "Idyllwild"]
    all_city_list = []
    key = "3d7c7bb9c21f35dc0201beb2b0f6970b"
    part = "minutely,alerts,daily,hourly,"
    for i in city_list:
        city_to_coord = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={i}&limit=5&appid={key}").json()
        city_name = city_to_coord[0]["name"]
        lat = city_to_coord[0]["lat"]
        lon = city_to_coord[0]["lon"]
        open_weather_api = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}&units=imperial"
        r = requests.get(f"{open_weather_api}").json()
        city_weather  = {
            'name' : city_name.replace("'", " "),
            'temp' : r['current']['temp'],
            'weather' : r['current']['weather'][0]['description'],
            'lat': r['lat'],
            'lon': r['lon']
        }
        all_city_list.append(city_weather)
    return render(request, 'webapp.html', {'data': all_city_list})

class CommentList(generic.ListView):
    queryset = Comment.objects.filter().order_by('-created_on')
    template_name = 'forum.html'

def forum_post(request):
    if request.method=='POST':
        name=request.POST['name']
        message=request.POST['message']
        comment=Comment.objects.create(name=name, message=message)
    return render(request,'forum_post.html')