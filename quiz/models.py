import re
import json
import csv
from django.db import models
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
from django.db.models.signals import pre_save, post_save
import io
from .signals import csv_uploaded
from .validators import csv_file_validator, question_file_validator
from django.contrib.auth.models import User
import mcq
from django.db.models import Q

User = settings.AUTH_USER_MODEL


# class CSVUpload(models.Model):
#     title       = models.CharField(max_length=100, verbose_name=_('Title'), blank=False)
#     user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     file        = models.FileField(upload_to=upload_csv_file, validators=[csv_file_validator])
#     completed   = models.BooleanField(default=False)
#     # questions   = models.BooleanField(default=True)
#     # students    = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

def create_user(data):
    user = User.objects.create_user(username=data['username'],
                            email=data['email'],
                            password=data['password'],
                            first_name=data['first_name'],
                            last_name=data['last_name']
                            )
    user.is_admin=False
    user.is_staff=False
    user.save()


def csv_upload_post_save(sender, instance, created, *args, **kwargs):
    if not instance.completed:
        csv_file = instance.file
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string, delimiter=';', quotechar='|')
        header_ = next(reader)
        header_cols = convert_header(header_)
        print(header_cols, str(len(header_cols)))
        parsed_items = []

        '''
        if using a custom signal
        '''
        for line in reader:
            # print(line)
            parsed_row_data = {}
            i = 0
            print(line[0].split(','), len(line[0].split(',')))
            row_item = line[0].split(',')
            for item in row_item:
                key = header_cols[i]
                parsed_row_data[key] = item
                i+=1
            create_user(parsed_row_data) # create user
            parsed_items.append(parsed_row_data)
            # messages.success(parsed_items)
            print(parsed_items)
        csv_uploaded.send(sender=instance, user=instance.user, csv_file_list=parsed_items)
        ''' 
        if using a model directly
        for line in reader:
            new_obj = YourModelKlass()
            i = 0
            row_item = line[0].split(',')
            for item in row_item:
                key = header_cols[i]
                setattr(new_obj, key) = item
                i+=1
            new_obj.save()
        ''' 
        instance.completed = True
        instance.save()

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EnrollmentModel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=None)
    employer_name = models.CharField(max_length=100, null=True)
    group_plan_number = models.CharField(max_length=10, null=True)
    ssn = models.CharField(max_length=10, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default='Male')
    date_of_birth = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    work_status = models.CharField(max_length=10, null=True)
    annual_income = models.IntegerField(null=True)
    profession = models.CharField(max_length=100, null=True)
    dependent_details = models.CharField(max_length=10, null=True)
          
    def __str__(self):
        return self.profession 

class ClaimModel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=None)
    group_id = models.CharField(max_length=10, null=True)
    ssn = models.CharField(max_length=10, null=True)
    claim_number = models.CharField(max_length=10, null=True)
          
    def __str__(self):
        return self.group_id


# post_save.connect(csv_upload_post_save, sender=CSVUpload)


