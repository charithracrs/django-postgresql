from django.shortcuts import render, redirect
from .models import Acrylic

# Create your views here.
def index(request):
    acrylics = Acrylic.objects.all()
    return render(request, 'index.html', {'acrylics' : acrylics})

def single(request):
    return render(request, 'single.html')

def view_picture(request):
    print(request.method)
    picture = request.GET['picture']
    if picture=='locked':
        return redirect('accounts/login')
    else:
        return render(request, 'view_picture.html', {'picture' : picture})