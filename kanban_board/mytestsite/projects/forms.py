from django import forms

class newTileForm(forms.Form):
    tileTitle = forms.CharField(label='tileTitle', max_length=100)
    tileAuthor = forms.CharField(label='tileAuthor', max_length=100)
    tileDescription = forms.CharField(label='tileDescription', max_length=100)

    
    CHOICES = [('Organizzativo', 'Organizzativo'),('Informativo', 'Informativo')]

    tileMessaggio = forms.CharField(label='tileMessaggio', widget=forms.RadioSelect(choices=CHOICES))
    #tileImg = forms.ImageField(label='tileImg')