# Generated by Django 3.2.4 on 2021-06-28 14:39

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_tile_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('nomeColonna', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Column',
            },
        ),
        migrations.AddField(
            model_name='tile',
            name='nomeColonna',
            field=models.TextField(default=0, verbose_name=django.db.models.fields.related.ForeignKey),
        ),
    ]
