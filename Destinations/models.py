from django.db import models

# Create your models here.
class Destinations(models.Model):
    dest_Division_Id = models.AutoField(primary_key =True) 
    division_Name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.division_Name

class Destinations_States(models.Model):
    states = models.CharField(max_length= 30)
    states_Id = models.AutoField(default=None, blank=True, null=False,primary_key = True)
    destination = models.ForeignKey(Destinations,on_delete = models.CASCADE)

    def __str__(self):
        return self.states

class Cities(models.Model):
    name = models.CharField(max_length = 30)
    states_Id = models.ForeignKey(Destinations_States,on_delete =models.CASCADE)
    

class Discription(models.Model):
    header_Title = models.CharField(max_length = 100)
    Discription = models.TextField()
    dest_id = models.ForeignKey(Destinations,on_delete = models.CASCADE , default = None,blank = True,null=True)
    dest_stat_id = models.ForeignKey(Destinations_States,on_delete = models.CASCADE, default = None,blank = True,null=True)
    city = models.ForeignKey(Cities,on_delete = models.CASCADE, default = None,blank = True,null=True)