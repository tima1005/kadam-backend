from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Create admin user"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.getenv("kadam", "admin")
        password = os.getenv("kadam")

        if not password:
            self.stdout.write(
                self.style.ERROR("kadam is not set")
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