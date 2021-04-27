from django import forms
class FacultyRegisterationform(forms.Form):
    Username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'textin'}))
    PhoneNumber=forms.CharField(max_length=100)
    Course=forms.CharField(max_length=100)
    Age=forms.CharField(max_length=50)
    Password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        Age=cleaned_data.get("Age")
        if int(Age)<18:
            msg="Invalid age"
            self.add_error("Age",msg)

class FacultyLoginForm(forms.Form):
    Username=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100)
