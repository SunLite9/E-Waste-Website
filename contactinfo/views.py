from django.shortcuts import render

# Create your views here.

def contactinfo(request):
    return render (request, 'contactinfo/contactinfo.html')