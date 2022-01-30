from django.contrib import admin
from .models import Useraccountsmodel, Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'gender', 'parent_name', 'date_of_birth',
                    'address', 'city', 'state', 'studentIdnumber',)
    list_filter = ('name_user', 'parent_name', 'date_of_birth',
                   'address', 'city', 'state', 'studentIdnumber',)
