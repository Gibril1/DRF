from django.db import models
from users.models import User

# Create your models here.
class Resource(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)


    def __str__(self) -> str:
        return self.content


class AdditionalResource(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

