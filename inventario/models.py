from django.db import models

class Año2024(models.Model):
    barrio = models.CharField(max_length=120)
    cantidad = models.IntegerField()
    mes = models.CharField(max_length=120)

class Año2023(models.Model):
    barrio2 = models.CharField(max_length=120)
    cantidad2 = models.IntegerField()
    mes2 = models.CharField(max_length=120)

class Año2022(models.Model):
    barrio3 = models.CharField(max_length=120)
    cantidad3 = models.IntegerField()
    mes3 = models.CharField(max_length=120)

class Año2021(models.Model):
    barrio4 = models.CharField(max_length=120)
    cantidad4 = models.IntegerField()
    mes4 = models.CharField(max_length=120)

class Año2020(models.Model):
    barrio5 = models.CharField(max_length=120)
    cantidad5 = models.IntegerField()
    mes5 = models.CharField(max_length=120)


