from django import forms
class NewBookForm(forms.Form):
    title=forms.CharField(label="Title", max_length=100, required=True, widget=forms.TextInput(attrs={'size': '20',
    'placeholder':'Enter the book title'}))
    price=forms.FloatField(label="Price", required=True, widget=forms.TextInput(attrs={'size': '20',
    'placeholder':'Enter the book price'}))
    author=forms.CharField(label="Author", max_length=100, required=True, widget=forms.TextInput(attrs={'size': '20',
    'placeholder':'Enter the book author'}))
    publisher=forms.CharField(label="Publisher", max_length=100, required=True, widget=forms.TextInput(attrs={'size': '20',
    'placeholder':'Enter the book publisher'}))

class SearchForm(forms.Form):
    title=forms.CharField(label="Title", max_length=100, required=True, widget=forms.TextInput(attrs={'size': '20',
    'placeholder':'Enter the book title'}))
