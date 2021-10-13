from django.http import HttpResponse
from .models import Obra
from .serializers import ObraSerializer, ObraUploadSerializer
from rest_framework import generics, viewsets, response
from rest_framework.views import APIView
from rest_framework import status
import csv, pandas as pd
import xlwt
import re

class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer


# class ExportObrasToCSV(APIView):
#     def get(self, request):

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="export-obras.csv"'
#         writer = csv.writer(response, delimiter=';')
        
#         writer.writerow(['id', 'titulo', 'editora', 'foto', 'autores', 'created_at'])

#         for data in Obra.objects.all().values_list('id', 'titulo', 'editora', 'foto', 'autores', 'created_at'):
#             print(data)
#             writer.writerow(data)

#         return response


class ExportObrasToXLS(APIView):
    def get(self, request):

        response = HttpResponse(content_type='text/csms-excel')
        response['Content-Disposition'] = 'attachment; filename="export-obras.xls"'
        
        wb = xlwt.Workbook(encoding='latin-1')
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


class UploadObraView(generics.CreateAPIView):
    serializer_class = ObraUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        file = serializer.validated_data['file']
        reader = pd.read_csv(file, encoding="utf-8", sep=';')
        print(reader)

        for _, row in reader.iterrows():
            if row['autores']:
                row_autores = re.sub(r"\[|\]|\'", "", row['autores'])
                row_autores = row_autores.split(',')
                for i in range(len(row_autores)):
                    row_autores[i] = row_autores[i].strip()

            Obra(
                titulo=row['titulo'],
                editora=row['editora'],
                foto=row['foto'],
                autores=row_autores
            ).save()

        return response.Response({"status": "success"}, status.HTTP_201_CREATED)