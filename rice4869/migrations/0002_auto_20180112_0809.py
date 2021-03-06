# Generated by Django 2.0 on 2018-01-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rice4869', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imochi1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=200)),
                ('rddw_16h', models.IntegerField(default=0)),
                ('rddw_24h', models.IntegerField(default=0)),
                ('rddw_48h', models.IntegerField(default=0)),
                ('rddw_72h', models.IntegerField(default=0)),
                ('rmo_16h', models.IntegerField(default=0)),
                ('rmo_24h', models.IntegerField(default=0)),
                ('rmo_48h', models.IntegerField(default=0)),
                ('rmo_72h', models.IntegerField(default=0)),
                ('sddw_16h', models.IntegerField(default=0)),
                ('sddw_24h', models.IntegerField(default=0)),
                ('sddw_48h', models.IntegerField(default=0)),
                ('sddw_72h', models.IntegerField(default=0)),
                ('smo_16h', models.IntegerField(default=0)),
                ('smo_24h', models.IntegerField(default=0)),
                ('smo_48h', models.IntegerField(default=0)),
                ('smo_72h', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Imochi',
        ),
    ]
