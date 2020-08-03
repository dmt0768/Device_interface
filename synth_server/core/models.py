from django.db import models

class Lines(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField(blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return 'Линия № ' + str(self.number)


