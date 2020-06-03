from django.db import models
from django.core.validators import RegexValidator

class Password(models.Model):
    password_id = models.AutoField(primary_key = True)
    password = models.CharField(max_length = 255, blank=False)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    password_id = models.ForeignKey(Password, on_delete = models.CASCADE)
    name = models.CharField(max_length = 45, blank = False, default = '')
    surname = models.CharField(max_length = 45, blank = False, default = '')
    mail = models.CharField(max_length = 45, blank = False, default = '')
    phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$',
                                 message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators = [phone_regex], max_length = 17, blank=True)

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

class Token(models.Model):
    token_id = models.AutoField(primary_key = True)
    token = models.CharField(max_length = 255)




class Image(models.Model):
    image_id = models.AutoField(primary_key=True)

