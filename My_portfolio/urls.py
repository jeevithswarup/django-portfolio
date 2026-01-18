from django.urls import path
from.views import *
urlpatterns = [
    path('',Home,name='Home'),
    path('contact/',contact,name='contact'),
    path('academics/',Academics,name='Academics'),
    path('project/',Project_details,name="Project"),
    path("project/<int:id>/",Project_details, name="Project"),
]

