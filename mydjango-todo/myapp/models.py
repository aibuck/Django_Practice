# from django.db import models

# # Create your models here.

# class Item(models.Model):
#   name = models.CharField(max_length=100)
#   complete = models.BooleanField(default=False)
#   created = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.name
  
#   class Meta:
#     ordering = ['complete']

from django.db import models

class Todo(models.Model) :
    content = models.CharField(max_length=50)
    completed = models.BooleanField()