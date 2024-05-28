from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('This field is required.')
        if email and CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
