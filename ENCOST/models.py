from django.db import models


class Client(models.Model):
    name = models.TextField(max_length=50)

    class Meta:
        db_table = 'clients'


class Duration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT)
    start = models.DateTimeField(auto_now=True)
    stop = models.DateTimeField(auto_now=True)
    mode = models.ForeignKey('Mode', on_delete=models.PROTECT)
    minutes = models.IntegerField()

    class Meta:
        db_table = 'durations'


class Equipment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    name = models.TextField(max_length=50)

    class Meta:
        db_table = 'equipment'


class Mode(models.Model):
    name = models.TextField(max_length=50)

    class Meta:
        db_table = 'modes'
