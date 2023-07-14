from django.db import models

class SendMessage(models.Model):
    name=models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=500)
    
