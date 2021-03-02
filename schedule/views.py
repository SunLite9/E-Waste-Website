from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BookAppointment
from django.core.mail import send_mail, EmailMessage

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
    return redirect('schedulepage')


# def sendemail2(request):
#     send_mail(
#         subject = f'{request.POST.get("username")}    {request.POST.get("pickupdate")}',
#         message = 'Name: {request.POST.get("username")}
# Email: {request.POST.get("email")}
# Phone Number: {request.POST.get("phonenumber")}
# Address: {request.POST.get("address")}
# Description: {request.POST.get("description")}
# Pickup Date: {request.POST.get("pickupdate")}
# Pickup Time: {request.POST.get("pickuptime")}
# Images: {request.FILES.get("image")},
#         from_email = "sunlite991@gmail.com",
#         recipient_list = ["makeacleanertomorrow@gmail.com", "ravikiran03.m@gmail.com"],
#         fail_silently = False
#
#     )

def sendemail(request):
    email= EmailMessage(
        subject='new booking',
        body=f'new booking from {request.POST.get("username")}',
        to= ["makeacleanertomorrow@gmail.com", "ravikiran03.m@gmail.com", "satyarth.shankar@gmail.com"]
    )
    image=request.FILES['image']
    email.attach('user image', image.read(), image.content_type)
    email.send()

