from django import forms

class newTileForm(forms.Form):
    tileTitle = forms.CharField(label='tileTitle', max_length=100)
    tileAuthor = forms.CharField(label='tileAuthor', max_length=100)
    tileDescription = forms.CharField(label='tileDescription', max_length=100, required=False)
    CHOICES = [('Organizzativo', 'Organizzativo'),('Informativo', 'Informativo')]
    tileMessaggio = forms.CharField(label='tileMessaggio', widget=forms.RadioSelect(choices=CHOICES))
    tileColumn = forms.CharField(label='tileColumn', max_length=100)


class newColumnForm(forms.Form):
    columnName = forms.CharField(label='columnName', max_length=100)


class moveTileForm(forms.Form):
    nomeTile = forms.CharField(label='nomeTile', max_length=100)
    nomeColonna = forms.CharField(label='nomeColonna', max_length=100) 
    contenuto = forms.CharField(label='contenuto', max_length=100) 

class modifyColumnForm(forms.Form):
    oldColumnName = forms.CharField(label='oldColumnName', max_length=100)
    newColumnName = forms.CharField(label='newColumnName', max_length=100) 


class modifyTileForm(forms.Form):
    tileTitle2 = forms.CharField(label='tileTitle2', max_length=100)
    tileColumn2 = forms.CharField(label='tileColumn2', max_length=100)

    tileTitleModify = forms.CharField(label='tileTitleModify', max_length=100)
    tileAuthorModify = forms.CharField(label='tileAuthorModify', max_length=100)
    tileDescriptionModify = forms.CharField(label='tileDescriptionModify', max_length=100)