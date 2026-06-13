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
        widgets = {
            "date_peremption": forms.DateInput(attrs={"type": "date"}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = ("nom", "prenom", "date_inscription", "adresse")
        labels = {
            "nom": _("Nom"),
            "prenom": _("Prenom"),
            "date_inscription": _("Date d'inscription"),
            "adresse": _("Adresse"),
        }
        widgets = {
            "date_inscription": forms.DateInput(attrs={"type": "date"}),
        }


class ImportProduitCsvForm(forms.Form):
    fichier = forms.FileField(label="Fichier CSV")


class CommandeForm(forms.Form):
    client = forms.ModelChoiceField(
        queryset=models.Client.objects.all().order_by("nom", "prenom"),
        label="Client",
        empty_label="-- Sélectionner un client --",
        widget=forms.Select(attrs={"style": "padding:6px; font-size:1em;"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        client = cleaned_data.get("client")
        if not client:
            raise forms.ValidationError("Veuillez sélectionner un client.")
        return cleaned_data

