from unicodedata import name
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from app1.models import Employee


# Create your views here.

def upload_file(request):
    if request.method == "POST" and request.FILES['up_file']:
        name = request.POST['name']
        email1 = request.POST['email1']
        desc = request.POST['desc']
        file1 = request.FILES['up_file']
        fs = FileSystemStorage()
        filename = fs.save(file1.name, file1)
        uploaded_file_url = fs.url(filename)

        data_store = Employee.objects.get_or_create(name= name, email = email1, desc = desc, document= filename)

        return render(request,'upload.html', {'uploaded_file_url':uploaded_file_url})


    return render(request,'upload.html')
