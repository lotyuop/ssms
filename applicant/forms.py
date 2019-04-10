from django.forms import ModelForm
from .models import Appstudent

class Application(ModelForm):
    class Meta:
        model=Appstudent
        fields="__all__"