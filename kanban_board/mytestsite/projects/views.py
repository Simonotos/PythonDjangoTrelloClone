import os
from django.db.models.expressions import Col, F
from django.forms.fields import ImageField, JSONString
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import modifyColumnForm, modifyTileForm, moveTileForm, newColumnForm, newTileForm
from .models import Column, SaveImage, Tile
from django.contrib import messages
from django.core import serializers
from django.core.files import File

from .import globalVariables

#Image
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


# Create your views here.

@csrf_exempt
def saveTile(request):
    print("Entri nel saveTile")

    if request.method == 'POST':

        trovato : bool = False

        while globalVariables.image == None:
            trovato = False

        form = newTileForm(request.POST)

        if form.is_valid():

            titolo : str = form.cleaned_data['tileTitle']
            autore : str = form.cleaned_data['tileAuthor']
            descrizione : str = form.cleaned_data['tileDescription']
            tipo_messaggio = form.cleaned_data['tileMessaggio']
            nomeColonna : str = form.cleaned_data['tileColumn']

            #Cerco se la colonna inserita dall'utente esiste
            nomeColonna : str = nomeColonna.replace(' ', '')
            nomeColonnaInput : str = nomeColonna.lower()

            oggetti_colonne = Column.objects.all()
            trovato = False

            for item in oggetti_colonne:
                nomeColonnaTile = item.nomeColonna.replace(' ', '')

                if nomeColonnaTile.lower() == nomeColonnaInput:
                    trovato = True
            
            if trovato == False:
                column = Column(nomeColonna = nomeColonnaInput)
                column.save()
            #Fine Cerco
            

            field_name = 'image'
            obj = SaveImage.objects.first()
            field_value = getattr(obj, field_name)
            stringa = str(field_value)
            stringa = stringa[16:]

            #Create Row
            tileRow = Tile(titolo = titolo, autore = autore, contenuto_testo = descrizione,contenuto_img =stringa ,tipo_messaggio = tipo_messaggio, nomeColonna = nomeColonnaInput)
            tileRow.save()
            #SaveImage.delete()
        else:
            print(form.errors)
            return HttpResponse(status = 404) #Stringa inserita non valida
        
    return HttpResponse("Created")
    

@csrf_exempt
def saveColumn(request):
    #print("Entri nel saveColumn")
    if request.method == 'POST':
        form = newColumnForm(request.POST)

        if form.is_valid():
            nomeColonna : str = form.cleaned_data['columnName']

            #Cerco se la colonna inserita dall'utente esiste
            nomeColonna : str = nomeColonna.replace(' ', '')
            nomeColonnaInput : str = nomeColonna.lower()
            oggetti_colonne = Column.objects.all()
            trovato = False

            for item in oggetti_colonne:
                nomeColonnaTile = item.nomeColonna.replace(' ', '')

                if nomeColonnaTile.lower() == nomeColonnaInput:
                    trovato = True
            
            if trovato == False:
                column = Column(nomeColonna = nomeColonnaInput)
                column.save()
        else:
            return HttpResponse(status = 404) #Stringa inserita non valida
        
        return HttpResponse("Colonna creata")



def index(request):
    #print("Entri nell'index")
    return render(request, 'index.html')


def getTiles(request):
    #print("popola tiles")
    
    if request.method == 'GET':
        lista1 = Tile.objects.all().values()
        lista2 = list(lista1)
        data = lista2
        return JsonResponse(data, safe=False)

def getColumns(request):
    #print("mostra colonne")

    if request.method == 'GET':
        data = list(Column.objects.filter(stato = "incorso").values())
        return JsonResponse(data, safe=False)

def getColumnsArchived(request):
    print("mostra colonne archiviate")

    if request.method == 'GET':
        data = list(Column.objects.filter(stato = "archiviata").values())
        return JsonResponse(data, safe=False)

def showPageArchivio(request):
    return render(request, 'colonneArchiviate.html')

@csrf_exempt
def moveTile(request):

    if request.method == 'POST':
        form = moveTileForm(request.POST)

        if form.is_valid():
                nomeTile : str = form.cleaned_data['nomeTile']
                nomeColonna : str = form.cleaned_data['nomeColonna']
                contenuto : str = form.cleaned_data['contenuto']

                print(nomeTile + nomeColonna + contenuto)

                #Cerco se la colonna inserita dall'utente esiste
                nomeColonna : str = nomeColonna.replace(' ', '')
                nomeColonnaInput : str = nomeColonna.lower()
                oggetti_colonne = Column.objects.all()
                trovata_colonna : bool = False

                for item in oggetti_colonne:
                    nomeColonnaTile = item.nomeColonna.replace(' ', '')
                    if nomeColonnaTile.lower() == nomeColonnaInput:
                        trovata_colonna = True
                        save_column = item

                #Cerco se il tile inserito dall'utente esiste
                nomeTile : str = nomeTile.replace(' ', '')
                nomeTileInput : str = nomeTile.lower()
                oggetti_tile = Tile.objects.all()
                trovato_tile : bool = False

                for item in oggetti_tile:
                    titoloTile = item.titolo.replace(' ', '')

                    if titoloTile.lower() == nomeTileInput:
                        contenutoTile  = item.contenuto_testo.replace(' ', '')
                        contenuto = contenuto.replace(' ', '')

                        if contenutoTile.lower() == contenuto.lower():
                            trovato_tile = True
                            save_tile = item

                if (trovato_tile == True & trovata_colonna == True):
                    save_tile.nomeColonna = nomeColonna
                    save_tile.save()
                elif (trovato_tile == False and trovata_colonna == False):
                    return HttpResponse(status = 404) #Tile o Colonna non presente'''

        else:
            return HttpResponse(status = 404) #Stringa inserita non valida
            
        return HttpResponse("Colonna creata")


@csrf_exempt
def modifyColumn(request):

    if request.method == 'POST':
        form = modifyColumnForm(request.POST)

        if form.is_valid():
                oldColumnName : str = form.cleaned_data['oldColumnName']
                newColumnName : str = form.cleaned_data['newColumnName']

                #Cerco se la colonna inserita dall'utente esiste
                oldColumnName : str = oldColumnName.replace(' ', '')
                oldColumnNameInput : str = oldColumnName.lower()

                newColumnName : str = newColumnName.replace(' ', '')
                newColumnNameInput : str = newColumnName.lower()

                oggetti_colonne = Column.objects.all()
                trovata_colonna : bool = False
                trovata_colonna_nuova : bool = False

                for item in oggetti_colonne:
                    nomeColonnaTile = item.nomeColonna.replace(' ', '')
                    if nomeColonnaTile.lower() == oldColumnNameInput:
                        trovata_colonna = True
                        save_column = item

                    if nomeColonnaTile.lower() == newColumnNameInput:
                        trovata_colonna_nuova = True

                if trovata_colonna == True and trovata_colonna_nuova == False:
                    save_column.delete()

                    column = Column(nomeColonna = newColumnName)
                    column.save()

                    oggetti_tile = Tile.objects.all()
                    
                    for obj in oggetti_tile:
                        if obj.nomeColonna == oldColumnName:
                            tileRow = Tile(titolo = obj.titolo, autore = obj.autore, contenuto_testo = obj.contenuto_testo,tipo_messaggio = obj.tipo_messaggio, nomeColonna = newColumnName)
                            tileRow.save()
                            obj.delete()
                else:
                    return HttpResponse(status = 404)
        else:
            return HttpResponse(status = 404) #Stringa inserita non valida

        return HttpResponse("Colonna creata")


@csrf_exempt
def modifyTile(request):

    if request.method == 'POST':
        form = modifyTileForm(request.POST)
        print("Ci entro")
        if form.is_valid():
                #Check data
                tileTitle2 : str = form.cleaned_data['tileTitle2']
                tileColumn2 : str = form.cleaned_data['tileColumn2'] 
                
                #Modify data
                tileTitleModify : str = form.cleaned_data['tileTitleModify']
                tileAuthorModify : str = form.cleaned_data['tileAuthorModify']
                tileDescriptionModify : str = form.cleaned_data['tileDescriptionModify']
                
                #Cerco se il tile con tale colonna esiste
                tileTitle2 : str = tileTitle2.replace(' ', '')
                tileTitle2Input : str = tileTitle2.lower()

                tileColumn2 : str = tileColumn2.replace(' ', '')
                tileColumn2Input : str = tileColumn2.lower()

                oggetti_tile = Tile.objects.all()
                trovato_tile : bool = False

                for item in oggetti_tile:
                    nomeTitleTile = item.titolo.replace(' ', '')
                    nomeColumnTile = item.nomeColonna.replace(' ', '')

                    if nomeTitleTile.lower() == tileTitle2Input and nomeColumnTile.lower() == tileColumn2Input:
                        trovato_tile = True
                        save_tile = item

                if trovato_tile == True:
                    save_tile.titolo = tileTitleModify
                    save_tile.autore = tileAuthorModify
                    save_tile.contenuto_testo = tileDescriptionModify
                    save_tile.save()
                else:
                    return HttpResponse(status = 404)
        else:
            return HttpResponse(status = 404) #Stringa inserita non valida

        return HttpResponse("Colonna creata")

@csrf_exempt
def deleteColumn(request):
    #print("deleteColumn")

    if request.method == 'POST':
        columnName : str = request.POST.get('param', None)
        columnName = columnName.replace(' ','')
        columnName = columnName.lower()

        objects_column = Column.objects.all()
        objects_tile = Tile.objects.all()

        for obj in objects_column:
            if obj.nomeColonna == columnName:
                obj.delete()

        for obj2 in objects_tile:
            if obj2.nomeColonna == columnName:
                obj2.delete()
            
    return HttpResponse("Colonna eliminata")

@csrf_exempt
def archiveColumn(request):
    print("archiveColumn")

    if request.method == 'POST':
        columnName : str = request.POST.get('param', None)
        columnName = columnName.replace(' ','')
        columnName = columnName.lower()

        objects_column = Column.objects.all()

        for obj in objects_column:
            if obj.nomeColonna == columnName:
                obj.stato = "archiviata"
                obj.save()
            
    return HttpResponse("Colonna eliminata")

@csrf_exempt
def restoreColumn(request):
    print("restoreColumn")

    if request.method == 'POST':
        columnName : str = request.POST.get('param', None)
        columnName = columnName.replace(' ','')
        columnName = columnName.lower()

        objects_column = Column.objects.all()

        for obj in objects_column:
            if obj.nomeColonna == columnName:
                obj.stato = "incorso"
                obj.save()
            
    return HttpResponse("Colonna ripristinata")

@csrf_exempt
def receiveImg(request):
    print("receiveImg")

    if request.method == 'POST':
        image = request.FILES.get('file')
        globalVariables.image = image
        save_img = SaveImage(image = image)
        save_img.save()

    return HttpResponse("T'apposto")



