from django.db import models

class Dropdown(models.Model):
    name = models.CharField(max_length=30)
    philter = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s = %s' % (self.name, self.philter)

    class Meta:
        ordering = ["id"]

