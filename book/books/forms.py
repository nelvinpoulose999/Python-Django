from django import forms
class BookForm(forms.Form):
    Book_Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Book Name'}),label='')
    Author_Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Author Name'}),label='')
    Book_Price=forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Book Price'}),label='')
    Pages=forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Pages'}),label='')
    Category=forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Category'}),label='')

    def clean(self):
        cleaned_data=super().clean()
        Book_Price=cleaned_data.get("Book_Price")
        Pages=cleaned_data.get('Number_of_Pages')
        if int(Book_Price)>300:
            msg='price is high'
            self.add_error('Book_Price',msg)
        # elif int(Pages)>300:
        #     msg="Too many pages"
        #     self.add_error("Number_of_Pages",msg)
