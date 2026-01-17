
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from django.http import HttpResponse

# Temporary view to create a superuser
def create_superuser(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='portfolio',
            email='portfolio@gmail.com',
            password='Chinta@761200'  # Change to a secure password
        )
        return HttpResponse("Superuser created successfully!")
    return HttpResponse("Superuser already exists!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('My_portfolio.urls')),
    path('create-admin/',create_superuser),
]
