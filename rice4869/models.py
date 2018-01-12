from django.db import models

# Create your models here.


class Imochi1(models.Model):
    gene_id = models.CharField(max_length=200)
    rddw_16h = models.IntegerField(default=0)
    rddw_24h = models.IntegerField(default=0)
    rddw_48h = models.IntegerField(default=0)
    rddw_72h = models.IntegerField(default=0)
    rmo_16h = models.IntegerField(default=0)
    rmo_24h = models.IntegerField(default=0)
    rmo_48h = models.IntegerField(default=0)
    rmo_72h = models.IntegerField(default=0)
    sddw_12h = models.IntegerField(default=0)
    sddw_24h = models.IntegerField(default=0)
    sddw_36h = models.IntegerField(default=0)
    sddw_48h = models.IntegerField(default=0)
    sddw_72h = models.IntegerField(default=0)
    smo_12h = models.IntegerField(default=0)
    smo_24h = models.IntegerField(default=0)
    smo_36h = models.IntegerField(default=0)
    smo_48h = models.IntegerField(default=0)
    smo_72h = models.IntegerField(default=0)

    def __str__(self):
        return self.gene_id
