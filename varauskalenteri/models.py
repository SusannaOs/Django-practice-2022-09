from django.db import models

# Create your models here.

class Tapahtuma(models.Model):
    otsikko = models.CharField(max_length=200)
    kuvaus = models.TextField()
    alku = models.DateTimeField()
    loppu = models.DateTimeField()
    
    def kesto(self):
        return self.loppu - self.alku