# Generated by Django 3.2.4 on 2021-06-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_tile_contenuto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='contenuto_img',
            field=models.TextField(),
        ),
    ]
