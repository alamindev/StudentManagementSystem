from django import forms
from django.db import models
from .models import Student, Category
from django.contrib.auth import get_user_model
User = get_user_model()

 
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure registered? We cannot find this user")
        return username 
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid Password")
        elif user is None:
            pass
        else:
            return password

class StudentRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = [
            
            'FirstName', 
            'LastName', 
            'Roll', 
            'Father_name',
            'Mother_name',
            'Registration',
            'gender',
            'date_of_birth',
            'village',
            'address',
            'Email'
            
         ]
class StudentPresentForm(forms.ModelForm):
    CHOICES = [('1', 'Regular'), ('2', 'UnRegular')]
    check_box = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Category
        fields = [
            'category',
            'Date',
            'In_Time',
            'Out_Time',
            'check_box'
        ]         
     
     