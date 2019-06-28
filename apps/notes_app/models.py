from django.db import models
from ..login_app.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    content = models.TextField() #Should likely remove this
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.id} {self.name}"
    
class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Category, related_name="subcategories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subcontent(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(Note, related_name="subcontents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)