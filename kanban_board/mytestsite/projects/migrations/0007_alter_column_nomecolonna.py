# Generated by Django 3.2.4 on 2021-06-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_column_nomecolonna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='nomeColonna',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]