from django import forms

from  .models import Hostel


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = "__all__"
