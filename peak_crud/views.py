
from django.shortcuts import render
from django.contrib.gis.geos import Polygon

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Peak
from .serializers import PeakSerializer



#welcome page with some examples
def welcome(request):
    return render(request, 'peak_crud/welcome.html')

""" class PeakCrudView(APIView):

    def get(self, *args, **kwargs):
        peaks = Peak.objects.all()
        serializer = PeakSerializer(peaks, many=True)
        return Response(serializer.data) """


class PeakCrudViewSet(ModelViewSet):
    """this class allow CRUD operation on peaks

    Args:
        ModelViewSet (any): ModelViewset from django_rest

    Returns:
        [Peak]: return list of peak with GET, CREATE with POST and data. DELETE, UPDATE, on particular peaks
    """
    serializer_class = PeakSerializer 
    def get_queryset(self):
        return Peak.objects.all()

class PeakInsideBoundingBox(APIView):
    """
    Returns a list of all **active** accounts in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: http://example.com/activating-accounts
    """

    parser_classes = [JSONParser]
    lookup_url_kwarg = "min_x"

    def post(self, request, format=None):

        try:
        # get the bounding box coordinates from body or url parameters
            if request.data:                
                min_x = request.data['min_x']
                min_y = request.data['min_y']
                max_x = request.data['max_x']
                max_y = request.data['max_y']

            else:                        
                
                min_x = request.query_params.get("min_x")
                min_y =request.query_params.get('min_y')
                max_x = request.query_params.get('max_x')
                max_y = request.query_params.get('max_y')
               
        except:
            return Response({"error":"please provide bounding box coordinates in body or URL"})

        # create the bounding box
        try:
            bbox = Polygon.from_bbox((min_x, min_y, max_x, max_y))
        except:
            return Response({"error":"bad bounding box coordinates, please provide bounding box coordinates in body or URL"})

        # get all the peaks inside the bounding box
        peaks = Peak.objects.filter(location__intersects=bbox).all()
        
        #use the serializer to serialize to JSON
        serializer = PeakSerializer(peaks, many=True)
        
        return Response(serializer.data)
            