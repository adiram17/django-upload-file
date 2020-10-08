from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    if request.method == 'POST' and request.FILES['uploaded_file']:
        uploaded_file = request.FILES['uploaded_file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        filename = fs.url(filename)
        return render(request, 'home.html', {
            'filename': filename
        })
    else:
        return render(request, 'home.html', {})
 