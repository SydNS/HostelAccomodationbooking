from django.forms import ModelForm
from .models import Bookhosteltable


class Bookhosteltableform(ModelForm):
    class Meta:
        model = Bookhosteltable
        fields = "__all__"
