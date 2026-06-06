from django.contrib import admin
from . import models

admin.site.register(models.Categorie)
admin.site.register(models.Produit)
admin.site.register(models.Client)
admin.site.register(models.Commande)
