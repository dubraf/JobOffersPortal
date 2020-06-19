from django.db import models
from django.core.validators import RegexValidator
from .validators import validate_image_file_extension
from django.contrib.auth.models import AbstractUser
from restApi.managers.userManager import UserManager

phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$',
                             message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 45, blank = False, default = '')
    surname = models.CharField(max_length = 45, blank = False, default = '')
    phone_number = models.CharField(validators = [phone_regex], max_length = 17, blank = True)
    isEmployer = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'phone_number', 'isEmployer']
    objects = UserManager()

    def __str__(self):
        return self.email

class CV(models.Model):
    cv_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    file = models.FileField(upload_to='cvs/%Y/%m/%d/')

class EmployerProfile(models.Model):
    profile_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    name = models.CharField(max_length = 45, blank = False)
    description = models.CharField(max_length = 2000, blank = True)
    phone_number = models.CharField(validators = [phone_regex], max_length = 17, blank = True)
    email = models.EmailField(max_length = 45, blank = False)
    address = models.CharField(max_length = 125, blank = False)
    website = models.URLField(blank = True)
    image = models.FileField(upload_to = 'photos', validators = [validate_image_file_extension], null = True)

class JobTag(models.Model):
    tag_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    name = models.CharField(max_length = 45, blank = False)

class JobOffer(models.Model):
    job_offer_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    employer_profile_id = models.ForeignKey(EmployerProfile, on_delete = models.PROTECT, null = True, blank = True)
    name = models.CharField(max_length = 45, blank = False)
    description = models.CharField(max_length = 2000, blank = True, default = '')
    expiration_date = models.DateTimeField('expiration date')
    salary = models.FloatField(blank = False)
    jobTags = models.ManyToManyField(JobTag)
    image = models.FileField(upload_to = 'photos', validators = [validate_image_file_extension], null = True)

class Image(models.Model):
    image_id = models.AutoField(primary_key = True)

class FavoriteJobOffer(models.Model):
    fav_job_offer_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    job_offers = models.ManyToManyField(JobOffer)