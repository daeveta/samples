from .models import Students
from django.forms import ModelForm, TextInput


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ["name", "surname", "grade"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Surname',
            }),
            "grade": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Grade',
            }),
        }
