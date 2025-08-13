from django.db import models

class State(models.Model):
    
    state_name = models.CharField()

class Capital(models.Model):

    capital_name = models.OneToOneField(State, on_delete=models.CASCADE)