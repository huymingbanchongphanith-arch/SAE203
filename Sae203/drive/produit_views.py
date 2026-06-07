import csv
import io
from decimal import Decimal, InvalidOperation

from django.db.models.deletion import RestrictedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ImportProduitCsvForm, ProduitForm
from . import models


def ajout(request):
    form = ProduitForm()
    return render(request, "drive/produit/ajout.html", {"form": form})


def traitement(request):
    pform = ProduitForm(request.POST)
    if pform.is_valid():
        pform.save()
        return HttpResponseRedirect("/drive/produits/")
    return render(request, "drive/produit/ajout.html", {"form": pform})


def index(request):
    liste = list(models.Produit.objects.all())
    return render(request, "drive/produit/index.html", {"liste": liste})


def affiche(request, id):
    produit = models.Produit.objects.get(pk=id)
    return render(request, "drive/produit/affiche.html", {"produit": produit})


def delete(request, id):
    produit = models.Produit.objects.get(pk=id)
    try:
        produit.delete()
    except RestrictedError:
        liste = list(models.Produit.objects.all())
        erreur = "Impossible de supprimer ce produit car il est utilise dans une commande."
        return render(request, "drive/produit/index.html", {"liste": liste, "erreur": erreur})
    return HttpResponseRedirect("/drive/produits/")


def update(request, id):
    produit = models.Produit.objects.get(pk=id)
    form = ProduitForm(produit.dico())
    return render(request, "drive/produit/update.html", {"form": form, "id": id})


def traitementupdate(request, id):
    pform = ProduitForm(request.POST)
    if pform.is_valid():
        produit = pform.save(commit=False)
        produit.id = id
        produit.save()
        return HttpResponseRedirect("/drive/produits/")
    return render(request, "drive/produit/update.html", {"form": pform, "id": id})


def import_csv(request):
    form = ImportProduitCsvForm()
    return render(request, "drive/produit/import_csv.html", {"form": form})


def traitement_import_csv(request):
    form = ImportProduitCsvForm(request.POST, request.FILES)
    erreurs = []
    nombre_importes = 0

    if form.is_valid():
        fichier = request.FILES["fichier"]
        contenu = fichier.read().decode("utf-8-sig")
        lecteur = csv.DictReader(io.StringIO(contenu), delimiter=";")

        for numero_ligne, ligne in enumerate(lecteur, start=2):
            try:
                categorie = models.Categorie.objects.get(id=ligne["categorie_id"])
                prix = Decimal(ligne["prix"].replace(",", "."))
                produit = models.Produit(
                    nom=ligne["nom"],
                    date_peremption=ligne.get("date_peremption") or None,
                    photo=ligne.get("photo") or None,
                    marque=ligne.get("marque") or None,
                    prix=prix,
                    categorie=categorie,
                )
                produit.save()
                nombre_importes += 1
            except KeyError as erreur:
                erreurs.append(f"Ligne {numero_ligne} : colonne manquante {erreur}")
            except models.Categorie.DoesNotExist:
                erreurs.append(f"Ligne {numero_ligne} : categorie introuvable")
            except (InvalidOperation, ValueError):
                erreurs.append(f"Ligne {numero_ligne} : prix ou date invalide")

        return render(
            request,
            "drive/produit/resultat_import.html",
            {"nombre_importes": nombre_importes, "erreurs": erreurs},
        )

    return render(request, "drive/produit/import_csv.html", {"form": form})
