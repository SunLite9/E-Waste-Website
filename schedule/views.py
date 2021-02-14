from django.shortcuts import render
from django.http import JsonResponse
from .models import BookAppointment
from django.core.mail import send_mail

# Create your views here.

def schedule(request):
    return render(request, 'schedule/schedule_page.html')

def bookappointment(request):
    print("works")
    name = request.POST.get("username")
    email = request.POST.get("email")
    phonenumber = request.POST.get("phonenumber")
    address = request.POST.get("address")
    description = request.POST.get("description")
    pickupdate = request.POST.get("pickupdate")
    pickuptime = request.POST.get("pickuptime")
    image = request.FILES.get("image")
    print(type(image))

    BookAppointment.objects.create(
        name = name,
        email = email,
        phonenumber = phonenumber,
        address = address,
        description = description,
        pickupdate = pickupdate,
        pickuptime = pickuptime,
        image = image,
    )
    sendemail(request)
    return render(request, 'schedule/schedule_page.html')


def sendemail(request):
    send_mail(
        subject = f'{request.POST.get("username")}    {request.POST.get("pickupdate")}',
        message = f'''Name: {request.POST.get("username")}
Email: {request.POST.get("email")}
Phone Number: {request.POST.get("phonenumber")}
Address: {request.POST.get("address")}
Description: {request.POST.get("description")}
Pickup Date: {request.POST.get("pickupdate")}
Pickup Time: {request.POST.get("pickuptime")}
Images: {request.FILES.get("image")}
''',
        from_email = "sunlite991@gmail.com",
        recipient_list = ["makeacleanertomorrow@gmail.com", "ravikiran03.m@gmail.com"],
        fail_silently = False

    )


