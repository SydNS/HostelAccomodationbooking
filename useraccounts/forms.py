from datetime import datetime
from typing import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.context_processors import request

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['gender'].required = True
        self.fields['parent_name'].required = True
        self.fields['address'].required = True
        self.fields['city'].required = True
        self.fields['level_of_study'].required = True
        self.fields['phonenumber'].required = True
        self.fields['reporting_date'].required = True
        self.fields['studentIdnumber'].required = True
        self.fields['state'].required = True

    class Meta:
        model = Student
        fields = ('name_user', 'gender', 'parent_name', 'date_of_birth',
                  'address', 'city', 'state', 'studentIdnumber', 'reporting_date',
                  'level_of_study', 'phonenumber',)
        widgets = {
            'date_of_birth': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control',
                                                    'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'reporting_date': forms.DateInput(format=('%m/%d/%Y'),
                                              attrs={'class': 'form-control',
                                                     'placeholder': 'Select a date',
                                                     'type': 'date'}),

        }

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

    # def clean_parent_name(self):
    #     parent_name = self.cleaned_data.get('parent_name')
    #     if parent_name.len<8 :
    #         raise forms.ValidationError('Name is not valid!')
    #     return parent_name

    # def clean_name_user(self):
    #     name_user = self.cleaned_data.get('name_user')
    #     if not request.user == name_user:
    #         raise forms.ValidationError('Name is not valid!')
    #     return name_user
