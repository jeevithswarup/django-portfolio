from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.views import *
urlpatterns = [
    path('',Home,name='Home'),
    path('contact/',contact,name='contact'),
    path('acadamics/',Acadamics,name='Acadamics'),
    path('project/',Project_details,name="Project"),
    path("project/<int:id>/",Project_details, name="Project"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )