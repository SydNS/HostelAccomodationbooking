from django import forms
from .models import Roommodel


class RoomForm(forms.ModelForm):
    class Meta:
        model = Roommodel
        fields = '__all__'
