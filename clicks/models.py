from django.db import models


class Clicks(models.Model):
    click_id = models.CharField(max_length=128)
    timestamp = models.IntegerField()
    type = models.CharField(max_length=128)
    campaign = models.IntegerField()
    banner = models.IntegerField()
    content_unit = models.IntegerField()
    network = models.IntegerField()
    browser = models.IntegerField()
    operating_system = models.IntegerField()
    country = models.IntegerField()
    state = models.IntegerField()
    city = models.IntegerField()
