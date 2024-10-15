from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),  # Corrected field name
            'info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add information'})  # Typo fixed in placeholder
        }


class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        user = User
        fields = ['email']