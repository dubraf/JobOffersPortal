from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from restApi.managers.userManager import UserManager

class User(AbstractUser):
    username = None
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 45, blank = False, default = '')
    surname = models.CharField(max_length = 45, blank = False, default = '')
    email = models.CharField(max_length = 45, blank = False, default = '')
    phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$',
                                 message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators = [phone_regex], max_length = 17, blank=True)
    isEmployer = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

class CV(models.Model):
    cv_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    file = models.FileField()

class Permission(models.Model):
    permissions_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    type = models.CharField(max_length = 45, blank = False)

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 45, blank = False)

class EmployerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)

class JobAdvertisement(models.Model):
    job_adv_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    profile_id = models.ForeignKey(EmployerProfile, on_delete = models.PROTECT)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length = 45, blank = False)
    description = models.CharField(max_length = 2000, blank = True, default = '')
    expiration_date = models.DateTimeField('expiration date')
    salary = models.FloatField(blank = False)

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)

