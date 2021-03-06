from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .forms import UploadModelForm
from .models import Photo

# Create your views here.

def index(request):
    photos = Photo.objects.all()
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/photos')

    context = {
        'photos': photos,
        'form': form
    }   

    return render(request, 'photos/index.html', context)