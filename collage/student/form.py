from django import forms
class StudentRegisterationForm(forms.Form):
    StudentName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Course=forms.CharField(widget=forms.TextInput(attrs={'class':'textin'}))
    Email=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100)

class StudentLoginForm(forms.Form):
    Username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Password=forms.CharField(max_length=100)