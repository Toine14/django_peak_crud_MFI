from django.contrib.gis.db.models import PointField
from .models import Peak
from rest_framework.serializers import ModelSerializer

from rest_framework_gis.serializers import GeoModelSerializer
from rest_framework import serializers

class PeakSerializer(ModelSerializer):
    location = GeoModelSerializer.geo_field = 'point'
    class Meta:
        model = Peak
        fields = ('id', 'name', 'elevation', 'location')