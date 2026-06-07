from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ("nom", "descriptif")
        labels = {
            "nom": _("Nom de la categorie"),
            "descriptif": _("Descriptif"),
        }


class ProduitForm(ModelForm):
    class Meta:
        model = models.Produit
        fields = ("nom", "date_peremption", "photo", "marque", "prix", "categorie")
        labels = {
            "nom": _("Nom du produit"),
            "date_peremption": _("Date de peremption"),
            "photo": _("Photo"),
            "marque": _("Marque"),
            "prix": _("Prix"),
            "categorie": _("Categorie"),
        }
        localized_fields = ("date_peremption",)
        widgets = {
            "date_peremption": forms.DateInput(attrs={"type": "date"}),
        }


class ImportProduitCsvForm(forms.Form):
    fichier = forms.FileField(label="Fichier CSV")
