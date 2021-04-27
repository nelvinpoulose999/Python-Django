from django import forms
class StudentRegisterForm(forms.Form):
    Firstname=forms.CharField(max_length=100)
    Lastname=forms.CharField(max_length=100)
    Course=forms.CharField(max_length=100)
    Phonenumber=forms.CharField(max_length=100)
    Age=forms.CharField(max_length=50)
    Password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        Age=cleaned_data.get('Age')
        if int(Age)<18:
            msg='invalid age'
            self.add_error('Age',msg)

class StudentLoginForm(forms.Form):
    Username=forms.CharField(max_length=100)
    Password=forms.CharField(widget=forms.PasswordInput)