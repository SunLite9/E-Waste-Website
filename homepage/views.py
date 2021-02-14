from django.shortcuts import render

# Create your views here.

def homepage_home(request):
    return render(request, 'homepage/homepage_web.html')

def about(request):
    return render(request, 'homepage/about_us.html')

def jumbotrontest(request):
    return render(request, 'homepage/newhomepage.html')


