from django.contrib import admin
from Destinations.models import Destinations,Destinations_States,Cities,Discription
# Register your models here.

class Dest(admin.ModelAdmin):
    list_display = ('dest_Division_Id','division_Name')

class Dest_Stat(admin.ModelAdmin):
    list_display = ('states','destination')

class city(admin.ModelAdmin):
    list_display = ('name','states_Id')
class Discp(admin.ModelAdmin):
    list_display = ('header_Title','Discription','dest_id','dest_stat_id','city')

admin.site.register(Destinations,Dest)
admin.site.register(Destinations_States,Dest_Stat)
admin.site.register(Cities,city)
admin.site.register(Discription,Discp)