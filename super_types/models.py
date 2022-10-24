from django.db import models


# Create your models here.
class SuperType(models.Model):
    type = models.CharField(max_length=200)

    # super_type = models.ForeignKey(Super, on_delete=models.CASCADE)
