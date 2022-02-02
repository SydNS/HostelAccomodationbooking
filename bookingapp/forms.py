from datetime import datetime

from django.forms import ModelForm
from django import forms

from .models import Bookhosteltable


class Bookhosteltableform(ModelForm):

    # hostel_name = models.ForeignKey('hostels.Hostel', on_delete=models.CASCADE)
    # customer_name = models.ForeignKey('useraccounts.Student', on_delete=models.CASCADE)
    # room_type = models.ForeignKey('roomsapp.Roommodel', on_delete=models.CASCADE)
    # duration = models.CharField(max_length=10, choices=DURATION_SEMESTER)
    # arrival_date = models.DateField(null=True, blank=True)
    # payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    class Meta:
        model = Bookhosteltable
        fields = '__all__'
        widgets = {
            'arrival_date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control',
                                                    'placeholder': 'Select a date',
                                                    'type': 'date'}),

        }

    def clean_join_year(self):
        arrival_date = self.cleaned_data.get('arrival_date')
        if not (2019 < arrival_date <= datetime.now().year):
            raise forms.ValidationError('Please enter valid Join year')
        return arrival_date
