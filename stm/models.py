from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=70)
	studentClass = models.CharField(max_length=70)
	rollNo = models.CharField(max_length=70)
	phone = models.CharField(max_length=12)
	email = models.EmailField(max_length=70)
	password = models.CharField(max_length=70)