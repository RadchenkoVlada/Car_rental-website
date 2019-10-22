from django.db import models

# Create your models here.
class Tutorial(models.Model):
       tutorial_title = models.CharField(max_length=200)
       tutorial_content = models.TextField()


       def __str__(self):
       	return self.tutorial_title
