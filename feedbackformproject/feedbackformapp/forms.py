from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Your Rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )

    feedback = forms.CharField(
        label='Enter your rating',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )
