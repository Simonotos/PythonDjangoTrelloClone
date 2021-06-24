from typing import NewType
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .forms import newTileForm
from .models import Tile
# Create your views here.


def saveTile(request):
    if request.method == 'POST':
        form = newTileForm(request.POST)

        if form.is_valid():
            titolo : str = form.cleaned_data['tileTitle']
            autore : str = form.cleaned_data['tileAuthor']
            descrizione : str = form.cleaned_data['tileDescription']
            #immagine = form.cleaned_data['tileImg']
            tipo_messaggio = form.cleaned_data['tileMessaggio']

            #Create Row
            tileRow = Tile(titolo = titolo, autore = autore, contenuto_testo = descrizione,tipo_messaggio = tipo_messaggio)
            tileRow.save()
        else:
            raise Http404("Stringa inserita non valida")

    return render(request, 'index.html',{})


def index(request):
    return render(request, 'index.html',{})