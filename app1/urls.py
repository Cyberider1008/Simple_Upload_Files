from django.urls import path 
from app1.views import upload_file

urlpatterns = [
    path('', upload_file, name="upload"),
]
