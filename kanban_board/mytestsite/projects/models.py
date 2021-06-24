from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Tile(models.Model):
    titolo = models.TextField()
    autore = models.TextField()
    contenuto_testo = models.TextField()
    contenuto_img = models.ImageField()
    tipo_messaggio = models.TextField()

    class Meta:
        db_table = "Tile"

    




