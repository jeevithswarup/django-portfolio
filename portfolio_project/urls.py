
from django.contrib import admin
from django.urls import path,include
# from ninja import NinjaAPI
# from My_portfolio.api import router as portfolio_router

# api = NinjaAPI()

# api.add_router("", portfolio_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('My_portfolio.urls'))
]
