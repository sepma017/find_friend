from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    birth = models.DateTimeField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'[{self.pk}] {self.name} ( {self.email} )'

    def get_absolute_url(self):
        return f'/friend/{self.pk}/'