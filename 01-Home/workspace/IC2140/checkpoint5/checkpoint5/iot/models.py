from django.db import models

# Create your models here.
class Event(models.Model):
    node_id = models.CharField(max_length=2)
    loc = models.CharField(max_length=10)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    hum = models.DecimalField(max_digits=5, decimal_places=2)
    light= models.DecimalField(max_digits=5, decimal_places=2)
    snd = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Event #{}'.format(self.id)