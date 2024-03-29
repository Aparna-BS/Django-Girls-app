from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateField(default=timezone.now())
	published_date = models.DateField(blank=True, null=True)

	def publish():
		self.published_date = timezone.now()
		self.save()

	def __self__():
		return self.title
