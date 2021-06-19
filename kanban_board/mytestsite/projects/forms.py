from django import forms

class NameForm(forms.Form):
    nickname = forms.CharField(label='nickname', max_length=100)