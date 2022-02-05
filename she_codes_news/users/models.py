from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str_(self):
        return self.username
