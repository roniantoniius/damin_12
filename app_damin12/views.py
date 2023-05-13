from django.shortcuts import render
from django.http import HttpResponse
from app_damin12.utils import damin_model

def beranda(request):
    return render(request, 'beranda.html')

def hasil(request):
    damin_model()
    return render(request, 'hasil.html')




# Create your views here.
