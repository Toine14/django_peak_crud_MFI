#from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class Peak(models.Model):
    name = models.CharField(max_length=255, null=True)
    elevation = models.IntegerField(null=True)
    location = models.PointField(geography=True, srid=4326,null=True)
    #objects = models.GeoQuerySet.as_manager()
