from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Create admin user"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME", "kadam")
        password = os.getenv("ADMIN_PASSWORD")

        if not password:
            self.stdout.write(
                self.style.ERROR("ADMIN_PASSWORD is not set")
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f"User '{username}' already exists."
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Superuser '{username}' created successfully."
            )
        )