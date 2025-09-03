from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "completed"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter todo"}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
