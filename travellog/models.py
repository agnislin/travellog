from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32) # Each field is represented by an instance of a Field class, like CharField
    password = models.CharField(max_length=32)



# The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.
