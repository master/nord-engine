from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255, unique=True)
    path = models.CharField(max_length=255)
    enabled = models.BooleanField()

    class Meta:
        ordering = ('name', )
        
    def __unicode__(self):
        return self.name
