# Generated by Django 2.1.3 on 2018-12-10 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181210_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='imagefun',
            new_name='image',
        ),
    ]
