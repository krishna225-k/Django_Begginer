from django import forms


class StudentDataForm(forms.Form):
    student_name = forms.CharField(
        label='Name: ',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Student Name',
                'class': 'form-control'
            }
        )
    )

    course_name = forms.CharField(
        label='Course Name ',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Course Name',
                'class': 'form-control'
            }
        )
    )

    course_fee = forms.IntegerField(
        label='Course Fee ',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Course Fee',
                'class': 'form-control'
            }
        )
    )

    institute_name = forms.CharField(
        label='Institute Name ',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Institute Name',
                'class': 'form-control'
            }
        )
    )

    location = forms.CharField(
        label='Location  ',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Location ',
                'class': 'form-control'
            }
        )
    )