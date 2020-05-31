from django.db import models

# Create your models here.

class AppChoose(models.Model):
    app_choices = models.CharField(max_length=50)
    url = models.CharField(default='myApp', max_length=50)
    def __str__(self):
        return self.app_choices


