from django import forms
from .models import StudentDetails,Course,Collage,Location,Institute,Branch, StudentMarks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentDataForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['first_name','last_name','email','mobile',
                  'fee','collage','course','branch','location','institute']

    def __init__(self, *args, **kwargs):
        super(StudentDataForm, self).__init__(*args, **kwargs)
        self.fields['branch'].empty_label = "Select"
        self.fields['course'].empty_label = "Select"
        self.fields['location'].empty_label = "Select"
        self.fields['collage'].empty_label = "Select"
        self.fields['institute'].empty_label = "Select"

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1',
                  'password2','email']

class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class AddCollage(forms.ModelForm):
    class Meta:
        model = Collage
        fields = '__all__'

class AddInstitution(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'

class AddLocation(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class AddBranch(forms.ModelForm):
    class Meta:
        model = Branch
        fields ='__all__'

# class AddMarks(forms.ModelForm):
#     class Meta:
#         model = StudentMarks
#         fields = ['telugu','hindi','english','science','maths','social','profile_pic']
class AddMarks(forms.Form):
    telugu = forms.IntegerField(
        label="Enter Telugu Marks",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Telugu Marks'
            }
        )
    )
    hindi = forms.IntegerField(
        label="Enter Hindi Marks",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Hindi Marks'
            }
        )
    )
    english = forms.IntegerField(
        label="Enter English Marks",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'English Marks'
            }
        )
    )
    maths = forms.IntegerField(
        label="Enter Maths Marks",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Maths Marks'
            }
        )
    )
    science = forms.IntegerField(
        label="Enter Science Marks",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Science Marks'
            }
        )
    )
    social = forms.IntegerField(
        label="Enter Social Marks",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Social Marks'
            }
        )
    )
