from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Create kadam user"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.getenv("kadam", "kadam")
        password = os.getenv("kadam")

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