from django.conf import settings
from django.db import models
from django.urls import reverse


class Application(models.Model):
	responses = (
		("No response", "No response"),
		("Rejected", "Rejected"),
		("Passed", "Passed"),
	)
	company_name = models.CharField(max_length=255)
	status = models.CharField(max_length=255,choices=responses)
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.company_name

	def get_absolute_url(self):
		return reverse("application_detail", kwargs={"pk": self.pk})