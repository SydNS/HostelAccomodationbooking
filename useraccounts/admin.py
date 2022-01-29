from django.contrib import admin
from .models import Useraccountsmodel, Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name_user','gender', 'father_name', 'date_of_birth', 'fee_receipt',
                    'address', 'city', 'state', 'pincode', 'join_year')
    list_filter = ('name_user', 'father_name', 'date_of_birth', 'fee_receipt',
                   'address', 'city', 'state', 'pincode', 'join_year')
