from django.db import models
# Create your models here.

class Event(models.Model):
	"""Event which users create"""
	Description = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	Event_name = models.CharField(max_length=48)
	Event_time = models.DateTimeField()
	Event_venue = models.CharField(max_length=100)
	Max_players = models.IntegerField()
	Players_registratered = models.IntegerField()

	def __str__(self):
		"""Return string representation(description of event) of model"""
		Players_registratered = 0
		return self.Description
	
class Participant(models.Model):
	"""Participants of one Event"""
	event = models.ForeignKey(Event,on_delete=models.CASCADE)
	text = models.TextField() 
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'participants'

	def __str__(self):
		if(len(self.text) > 50):
			return self.text[:50] + "..."
		else:
			return self.text
