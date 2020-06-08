from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.models.ManyToManyField("Recipe", related_name=_("favorite"), blank=True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    time_required = models.CharField(max_length=20)
    description = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title