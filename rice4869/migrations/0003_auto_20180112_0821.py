# Generated by Django 2.0 on 2018-01-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rice4869', '0002_auto_20180112_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imochi1',
            old_name='sddw_16h',
            new_name='sddw_12h',
        ),
        migrations.RenameField(
            model_name='imochi1',
            old_name='smo_16h',
            new_name='sddw_36h',
        ),
        migrations.AddField(
            model_name='imochi1',
            name='smo_12h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imochi1',
            name='smo_36h',
            field=models.IntegerField(default=0),
        ),
    ]
