from django import forms
from .models import Student

# class StudentForm(forms.Form):
#  firstName = forms.CharField(label="firstname", max_length=20, required=True)
# lastName = forms.CharField(label="lastName", max_length=20,required=True)
# email = forms.EmailField(label="Email",required=True)
# age = forms.ImageField(label="age", required=True)
class studentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstName', 'lastname','email','age']
