from django.db import models

class PageMetaData(models.Model):	
	title = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	keywords = models.CharField(max_length=200, null=True)
	url		= models.CharField(max_length=200)