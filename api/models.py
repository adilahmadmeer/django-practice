from django.db import models


class asset(models.Model):
    mac_address = models.CharField(max_length=17)  # e.g. "AA:BB:CC:DD:EE:FF"
    owner = models.CharField(max_length=100)
    status = models.CharField(max_length=50)