"""EwasteNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import homepage.views
import schedule.views
import contactinfo.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('old/', homepage.views.homepage_home, name = 'homepage1'),
    path('about/', homepage.views.about, name = 'aboutpage' ),
    path('schedule/', schedule.views.schedule, name = 'schedulepage'),
    path('contactinfo/', contactinfo.views.contactinfo, name = 'contactinfopage'),
    path('blog/', blog.views.blog, name = 'blogpage'),
    path('bookappointment/', schedule.views.bookappointment, name='bookappointment'),
    path('', homepage.views.jumbotrontest, name='jumbotrontest')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


