from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .forms import NameForm

from .models import Nomi
# Create your views here.

def getNickname(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            stringa : str = form.cleaned_data['nickname']
            print(stringa)
            tabella_nomi = Nomi(name = stringa)
            tabella_nomi.save()
        else:
            raise Http404("Stringa inserita non valida")

    return render(request, 'index.html',{})