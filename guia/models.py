from django.db import models
from django.utils import timezone

# These Models maps the medical guide from  
# http://www.e-saude.iasep.pa.gov.br/guiamedico/guia.cfm

class City(models.Model):

    id = models.CharField(primary_key=True, max_length=4, unique=True)
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "cities"
    

class Service(models.Model):

    id = models.CharField(primary_key=True, max_length=4, unique=True)
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Place(models.Model):
    
    city =  models.ForeignKey('City', on_delete=models.CASCADE)
    service =  models.ForeignKey('Service', on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    adress = models.CharField(max_length=180)
    phone = models.CharField(max_length=120)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        unique_together = ["name", "city", "service"]
