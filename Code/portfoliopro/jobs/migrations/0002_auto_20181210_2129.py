# Generated by Django 2.1.3 on 2018-12-10 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='image',
            new_name='imagefun',
        ),
    ]
