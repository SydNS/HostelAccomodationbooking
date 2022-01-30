from django.forms import ModelForm
from .models import Bookhosteltable


class Bookhosteltableform(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['uid'].required = True
    #     self.fields['gender'].required = True
    #     self.fields['parent_name'].required = True
    #     self.fields['address'].required = True
    #     self.fields['city'].required = True
    #     self.fields['level_of_study'].required = True
    #     self.fields['phonenumber'].required = True
    #     self.fields['reporting_date'].required = True
    #     self.fields['studentIdnumber'].required = True
    #     self.fields['state'].required = True

    class Meta:
        model = Bookhosteltable
        fields = "__all__"
