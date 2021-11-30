from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'mobile', 'marks', 'college', 'course', 'branch', 'location']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['college'].empty_label = 'Select'
        self.fields['course'].empty_label = 'select'
        self.fields['branch'].empty_label = 'select'
        self.fields['location'].empty_label = 'select'

