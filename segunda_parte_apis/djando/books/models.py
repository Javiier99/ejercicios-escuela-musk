from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    parrafo = models.CharField(max_length=100)
    ibm_loquesea = models.CharField(max_length=13)

    def __str__(self):
        return self.title