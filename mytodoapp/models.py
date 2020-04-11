from django.db import models

# Create your models here.
class Todomodel(models.Model):
	taskname=models.CharField(max_length=100)
	targetdate=models.DateField()
	taskdescp=models.TextField()
	youremail=models.EmailField(default="kanak@gmail.com")