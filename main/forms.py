from django import forms


class GenerateForm(forms.Form):
    name = forms.CharField(
        help_text="Enter your name")
