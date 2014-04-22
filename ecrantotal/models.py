import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Create your models here

class Movies(models.Model):
	title = models.CharField(max_length=200)
	released = models.DateTimeField('date published')
	imdb = models.CharField(max_length=32)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.title


class Peoples(models.Model):
	name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	imdb = models.CharField(max_length=32)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

# Movie comments
class Comments(models.Model):
	movie = models.ForeignKey(Movies)
	comment = models.CharField(max_length=250)

# Youtube link to the trailer
class Trailer(models.Model):
	movie = models.ForeignKey(Movies)
	url = models.CharField(max_length=250)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.url

# Various movie related urls
class Links(models.Model):
	movie = models.ForeignKey(Movies)
	url = models.CharField(max_length=250)
	comment = models.CharField(max_length=250)
	#trailer, image, etc
	urltype = models.CharField(max_length=250)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.url