from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from LSM import views

router = routers.DefaultRouter()
router.register(r'obras', views.ObraViewSet, basename='Obras')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('file-obras/', views.ExportObrasToXLS.as_view(), name='file-obras'),
    path('upload-obras/', views.UploadObraView.as_view(), name='upload-obras')
]
