from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    
    country_name = models.CharField(max_length=255 , null=True, blank=True)
    country_information=models.CharField(max_length=255 , null=True,blank=True)


class Location(models.Model):
    
    city        = models.CharField(max_length=255, null=True, blank=True)
    address     = models.CharField(max_length = 255, null=True, blank=True)
    country     = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='locations')

class Users(models.Model):
    class Meta:
        verbose_name_plural = "Users"

    ADMIN = 'admin'
    VIEWER = 'viewer'
    USER_ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (VIEWER, 'Viewer'),
    ]    
        
    first_name   = models.CharField(max_length=255 , null=True, blank=True)
    last_name    = models.CharField(max_length=255 , null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email        = models.EmailField(null=True, blank=True)
    location     = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='users')
    role         = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default=VIEWER)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email} - {self.role}'


class Projects(models.Model):
    class Meta:
        verbose_name_plural = "Projects"
        
    name        = models.CharField(max_length=255, null=True, blank=True)
    type        = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self.name
    

class Devices(models.Model):
    class Meta:
        verbose_name_plural = "Devices"
        
    name      = models.CharField(max_length=255, null=True, blank=True)
    type      = models.CharField(max_length=255, null=True, blank=True)
   
         

    def __str__(self):
        return self.name    
    
class Data_returned(models.Model):
    class Meta:
        verbose_name_plural = "Data"

    energy     = models.FloatField(null=True, blank=True)
    power      = models.FloatField(null=True, blank=True)
    date_time  = models.DateTimeField(null=True, blank=True)
    device     = models.ForeignKey(Devices, on_delete=models.PROTECT, related_name='data_entries')

    def __str__(self):
        return f'Data - {self.date_time}'    
        
class Projects_user(models.Model):
    user     = models.ManyToManyField(Users)
    projects = models.ManyToManyField(Projects)
    ADMIN = 'admin'
    VIEWER = 'viewer'
    USER_ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (VIEWER, 'Viewer'),
    ]

    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default=VIEWER)

class Projects_device(models.Model):
    device  = models.ManyToManyField(Devices)
    projects= models.ManyToManyField(Projects)

class projects_location(models.Model):
    location  = models.ManyToManyField(Location)
    projects= models.ManyToManyField(Projects)
