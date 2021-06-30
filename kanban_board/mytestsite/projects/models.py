from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class SaveImage(models.Model):
    image = models.ImageField(upload_to='projects/static/')
    
    class Meta:
        db_table = "SaveImage"

class Tile(models.Model):
    titolo = models.TextField()
    autore = models.TextField()
    contenuto_testo = models.TextField()
    contenuto_img = models.TextField()
    tipo_messaggio = models.TextField()
    nomeColonna = models.TextField(ForeignKey, default=0)

    class Meta:
        db_table = "Tile"


class Column(models.Model):
    nomeColonna = models.TextField(primary_key=True)
    stato = models.TextField(default="incorso")

    class Meta:
        db_table = "Column"
    




