from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, surname, phone_number, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surname = surname,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_emplyeruser(self, email, name, surname, phone_number, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surname = surname,
            phone_number = phone_number
        )
        user.isEmployer = True
        user.save(using = self._db)
        return user

    def create_superuser(self, email, name, surname, phone_number, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            phone_number=phone_number
        )
        user.admin = True
        user.save(using=self._db)
        return user