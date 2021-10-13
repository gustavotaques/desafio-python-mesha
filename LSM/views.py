from django.http import HttpResponse
from .models import Obra
from .serializers import ObraSerializer
from rest_framework import response, viewsets
from rest_framework.views import APIView
import csv
import xlwt

class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer


# class ExportCSVObras(APIView):
#     def get(self, request):

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="export-obras.csv"'
#         writer = csv.writer(response)
        
#         writer.writerow(['id', 'titulo', 'editora', 'foto', 'autores', 'created_at'])

#         for data in Obra.objects.all().values_list('id', 'titulo', 'editora', 'foto', 'autores', 'created_at'):
#             print(data)
#             writer.writerow(data)

#         return response


class ExportCSVObras(APIView):
    def get(self, request):

        response = HttpResponse(content_type='text/csms-excel')
        response['Content-Disposition'] = 'attachment; filename="export-obras.xls"'
        
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Obras")
        row_num = 0

        colums = ['id', 'titulo', 'editora', 'foto', 'autores', 'created_at']

        for col_num in range(len(colums)):
            ws.write(row_num, col_num, colums[col_num])
        
        rows = Obra.objects.all().values_list('id', 'titulo', 'editora', 'foto', 'autores', 'created_at')

        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]))
        
        wb.save(response)

        return response