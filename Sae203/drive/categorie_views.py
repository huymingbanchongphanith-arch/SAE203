from django.http import HttpResponseRedirect
from django.db.models.deletion import RestrictedError
from django.shortcuts import render
from .forms import CategorieForm
from . import models


def ajout(request):
    form = CategorieForm()
    return render(request, "drive/categorie/ajout.html", {"form": form})


def traitement(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        cform.save()
        return HttpResponseRedirect("/drive/categories/")
    return render(request, "drive/categorie/ajout.html", {"form": cform})


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, "drive/categorie/index.html", {"liste": liste})


def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    liste = models.Produit.objects.filter(categorie_id=id)
    return render(request, "drive/categorie/affiche.html", {"categorie": categorie, "liste": liste})


def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    try:
        categorie.delete()
    except RestrictedError:
        liste = list(models.Categorie.objects.all())
        erreur = "Impossible de supprimer cette categorie car elle contient des produits."
        return render(request, "drive/categorie/index.html", {"liste": liste, "erreur": erreur})
    return HttpResponseRedirect("/drive/categories/")


def update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CategorieForm(categorie.dico())
    return render(request, "drive/categorie/update.html", {"form": form, "id": id})


def traitementupdate(request, id):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/drive/categories/")
    return render(request, "drive/categorie/update.html", {"form": cform, "id": id})
