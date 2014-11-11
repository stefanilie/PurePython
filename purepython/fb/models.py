from django.db import models

class UserPost(models.Model):
	text = models.TextField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	author=models.CharField(default='EdW', max_length=20)

# Create your models here.
