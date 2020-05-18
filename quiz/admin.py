from django.contrib import admin
from .models import ContactModel, EnrollmentModel, ClaimModel


admin.site.register(ContactModel)
admin.site.register(EnrollmentModel)
admin.site.register(ClaimModel)