from django.db import models

class Userdata(models.Model):
	key = models.CharField(max_length=50)
	url = models.TextField()

	def __str__(self):
		return self.key

class Crawldata(models.Model):
	key = models.ForeignKey(Userdata)
	brief = models.TextField()
	url = models.TextField()
	