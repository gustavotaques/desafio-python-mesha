from django.http import HttpResponse
from .models import Obra
from .serializers import ObraSerializer
from rest_framework import response, viewsets
from rest_framework.views import APIView
import csv

class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer


class ExportCSVObras(APIView):
    def get(self, request, *args, **kwargs):
        obras = Obra.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export-obras.csv"'
        writer = csv.writer(response)
        
        for obra in obras:
            print(obra)

        return response