from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return render(request,  'generator/index.html')
# Create your views here.
