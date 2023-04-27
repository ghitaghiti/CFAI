from django.db import models
from django.contrib.auth.models import User


class Code(models.Model):
	user = models.ForeignKey(User, related_name="code", on_delete=models.DO_NOTHING)
	question = models.TextField(max_length=5000)
	code_answer = models.TextField(max_length=5000)
	language = models.CharField(max_length=50)


	def __str__(self):
		return self.question
	

class Slider(models.Model):
	title= models.CharField(max_length=100, blank=False)
	description= models.TextField(max_length=800, blank=False)
	image= models.ImageField(upload_to='./static/slider', blank=False)

	def __str__(self):
		return self.title

