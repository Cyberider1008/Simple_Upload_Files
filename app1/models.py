from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    desc = models.CharField(max_length=50, blank = True)
    document = models.FileField(null =True, blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name