from django import forms

class FilterNameForm(forms.Form):
    filter_name = forms.CharField()
    
