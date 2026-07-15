from django.db import models


class asset(models.Model):
    id = models.IntegerField(primary_key=True)
    mac = models.CharField(max_length=50, null=True, blank=True)
    ip_address1 =  models.CharField(max_length=50)
    ip_address2 = models.GenericIPAddressField(null=True, blank=True)
    ip_address3 = models.GenericIPAddressField(null=True, blank=True)
    ip_address4 = models.GenericIPAddressField(null=True, blank=True)
    ip_address5 = models.GenericIPAddressField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.mac if self.mac else "Draft Asset"