from django.contrib import admin
from .models import Customer
from .models import Employee

admin.site.site_header = 'Admin CateCenter4U'
# Register your models here.

admin.site.register(Customer)
admin.site.register(Employee)
