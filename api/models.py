from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return '{}:{}'.format(self.name, self.is_vip)