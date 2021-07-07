from django.db import models

# Create your models here.
class Contactcarrers(models.Model):
	Name=models.CharField(max_length=30)
	PhoneNumber=models.IntegerField()
	Email=models.CharField(max_length=100)
	Message=models.CharField(max_length=100)

class Contactservices(models.Model):
	Name=models.CharField(max_length=30)
	PhoneNumber=models.IntegerField()
	Email=models.CharField(max_length=100)
	Message=models.CharField(max_length=100)

class Contactprojects(models.Model):
	Name=models.CharField(max_length=30)
	PhoneNumber=models.IntegerField()
	Email=models.CharField(max_length=100)
	Message=models.CharField(max_length=100)

class Video(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(upload_to="video/%y")
	def __str__(self):
		return self.caption