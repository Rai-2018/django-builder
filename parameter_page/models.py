from django.db import models

# Create your models here.
class ParameterModel(models.Model):
	First_Parameter = models.CharField(max_length=20)
	Second_Parameter = models.CharField(max_length=20)
	Third_Parameter = models.CharField(max_length=20)
