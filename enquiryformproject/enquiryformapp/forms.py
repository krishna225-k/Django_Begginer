from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):

    name = forms.CharField(
        label = "Enter your Name",
        widget = forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter your Name",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile number'
            }
        )
    )

    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )

    )

    COURSES_CHOICES = (
        ('Python', 'PYTHON'),
        ('Django', 'DJANGO'),
        ('UI', "UI"),
        ('Rest Api', 'REST API')
    )

    courses = MultiSelectFormField(choices=COURSES_CHOICES,
                                   label="Select YOur required courses")

    TRAINERS_CHOICES = (
        ('Narayana','NARAYANA'),
        ('Srinivas','SRINIVAS'),
        ('Mohan Reddy','MOHAN REDDY'),
        ('Wilson','WILSON')
    )

    trainers = MultiSelectFormField(choices=TRAINERS_CHOICES,
                                    label='Select Your required trainers')

    SHIFT_CHOICES = (
        ('Morning','MORNING'),
        ('Evening','EVENING'),
        ('Night','NIGHT')
    )

    shifts = MultiSelectFormField(choices=SHIFT_CHOICES,
                                  label="Select Required Shifts")

    LOCATIONS_CHOICES = (
        ('Ameerpet','AMEERPET'),
        ('Madhapur','MADHAPUR'),
        ('Kphb','KPHB'),
        ('Uppal','UPPAL')
    )

    locations = MultiSelectFormField(choices=LOCATIONS_CHOICES,label='Select Required Locations')

    GENDER_CHOICES = (
        ('Male','MALE'),
        ('Female','FEMALE')
    )

    gender = forms.CharField(
        label= "Enter your gender",
        widget= forms.RadioSelect(
            choices= GENDER_CHOICES
        )
    )

    start_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        label='Enter your Comfortable Timings:'
    )
