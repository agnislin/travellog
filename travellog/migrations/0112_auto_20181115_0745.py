# Generated by Django 2.1.3 on 2018-11-15 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travellog', '0111_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='path',
            new_name='file',
        ),
    ]
