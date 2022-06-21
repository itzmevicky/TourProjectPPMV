from django.test import TestCase

# Create your tests here.
from django.models import Destinations,Destinations_States,Cities,Discription
# Create your views here.
def getStates(name):
    states = Destinations.objects.filter(destination__division_Name =name)
    for x in states:
        print(x)


getStates('East')