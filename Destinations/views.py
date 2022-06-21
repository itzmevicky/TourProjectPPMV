from django.shortcuts import render,HttpResponse
from Destinations.models import Destinations,Destinations_States
# Create your views here.
def index(request):
    states = Destinations_States.objects.filter(destination__division_Name = 'East') 
    context = {
        'names' : states
    }
    return render(request,'Home.html',context)