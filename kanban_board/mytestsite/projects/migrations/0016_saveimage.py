# Generated by Django 3.2.4 on 2021-06-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_tile_contenuto_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'SaveImage',
            },
        ),
    ]
