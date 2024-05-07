from django.db import models

from django.db import models

class Todo(models.Model) :
    content = models.CharField(max_length=50)
    completed = models.BooleanField()