# Generated by Django 3.2.4 on 2021-06-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_column_nomecolonna'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='stato',
            field=models.TextField(default='inCorso'),
        ),
    ]