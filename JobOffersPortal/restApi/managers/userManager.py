from django.contrib.auth.models import  BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, surname, phone_number, isEmployer, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surname = surname,
            phone_number = phone_number,
            isEmployer = isEmployer
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_employeruser(self, email, name, surname, phone_number, isEmployer, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surname = surname,
            phone_number = phone_number,
            isEmployer = isEmployer
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