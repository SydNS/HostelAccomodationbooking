from datetime import datetime
from typing import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


# Create your forms here.
from .models import Student


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# profile registering form

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('gender', 'father_name', 'date_of_birth', 'fee_receipt',
                  'address', 'city', 'state', 'pincode', 'join_year')

    def clean_join_year(self):
        join_year = self.cleaned_data.get('join_year')
        if not (2019 < join_year <= datetime.now().year):
            raise forms.ValidationError('Please enter valid Join year')
        return join_year

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        if not len(str(pincode)) == 6:
            raise forms.ValidationError('Please enter valid Pincode')
        return pincode

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        if not re.match(r'[A-Za-z]{3,}', father_name):
            raise forms.ValidationError('Name is not valid!')
        return father_name

