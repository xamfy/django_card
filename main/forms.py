from django import forms


class GenerateForm(forms.Form):
    name = forms.CharField(label='name',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
