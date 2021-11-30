from django import forms
from .models import RegistrationData


class RegistrationForm(forms.Form):
    firstname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your First Name'
            }
        )
    )

    lastname = forms.CharField(
        label='last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your last Name'
            }
        )
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your user Name'
            }
        )
    )

    email = forms.EmailField(
        label='Email address ',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your password '
            }
        )
    )

    password2 = forms.CharField(
        label=' Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' password again'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your mobile'
            }
        )
    )
    ''' Here the limitation of len() function : i.e len() will find the length of string not for INT() or NUMBER'''
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = RegistrationData.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is already taken')
        elif len(username) >= 5:
            raise forms.ValidationError('UserName must have more than five characters')

        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = RegistrationData.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already taken')

        elif not 'gmail.com' in email:
            raise forms.ValidationError('Email ends with gmail.com domain name')
        else:
            return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        qs = RegistrationData.objects.filter(mobile=mobile)
        if qs.exists():
            raise forms.ValidationError('Mobile number already taken')
        elif len(str(mobile)) != 10:
            raise forms.ValidationError('Mobile Number should be 10 digits')

        else:
            return mobile

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise forms.ValidationError('password must match')

        elif len(str(password1)) <= 5 or len(str(password2)) >= 10:
            raise forms.ValidationError('password lenght must be more than 5 character and'
                                        ' less than 10 letters')

        else:
            return data
