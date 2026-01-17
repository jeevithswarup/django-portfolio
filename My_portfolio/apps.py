from django.apps import AppConfig
import os

class MyPortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'My_portfolio'

    def ready(self):
        if os.environ.get("CREATE_SUPERUSER") == "true":
            from django.contrib.auth import get_user_model
            User = get_user_model()

            username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
            email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
            password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

            if username and not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
