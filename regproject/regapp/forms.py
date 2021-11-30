from django import forms

class RegisterForm(forms.Form):

    first_name = forms.CharField(
        label='Enter your first name',
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Your first name'
            }
        )
    )

    last_name = forms.CharField(
        label='Enter your last name',
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Your last name'
            }
        )
    )

    username = forms.CharField(
        label= ' Enter your username',
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )

    password = forms.CharField(
        label= 'Enter your password',
        widget= forms.PasswordInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Your Password'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Your email",
        widget= forms.EmailInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Your email'
            }
        )
    )

    mobile = forms.IntegerField(
        label = ' Enter your Mobile Number',
        widget= forms.NumberInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Your mobile'
            }
        )

    )


class LoginForm(forms.Form):

    username = forms.CharField(
        label= "Enter your username",
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )

    password = forms.CharField(
        label= "Enter your passowrd",
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )