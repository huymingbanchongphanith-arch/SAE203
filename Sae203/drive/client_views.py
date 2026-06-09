from django.db.models.deletion import RestrictedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ClientForm
from . import models


def ajout(request):
    form = ClientForm()
    return render(request, "drive/client/ajout.html", {"form": form})


def traitement(request):
    cform = ClientForm(request.POST)
    if cform.is_valid():
        cform.save()
        return HttpResponseRedirect("/drive/clients/")
    return render(request, "drive/client/ajout.html", {"form": cform})


def index(request):
    liste = list(models.Client.objects.all())
    return render(request, "drive/client/index.html", {"liste": liste})


def affiche(request, id):
    client = models.Client.objects.get(pk=id)
    liste = models.Commande.objects.filter(client_id=id)
    return render(request, "drive/client/affiche.html", {"client": client, "liste": liste})


def delete(request, id):
    client = models.Client.objects.get(pk=id)
    try:
        client.delete()
    except RestrictedError:
        liste = list(models.Client.objects.all())
        erreur = "Impossible de supprimer ce client car il possede des commandes."
        return render(request, "drive/client/index.html", {"liste": liste, "erreur": erreur})
    return HttpResponseRedirect("/drive/clients/")


def update(request, id):
    client = models.Client.objects.get(pk=id)
    form = ClientForm(
        {
            "nom": client.nom,
            "prenom": client.prenom,
            "date_inscription": client.date_inscription,
            "adresse": client.adresse,
        }
    )
    return render(request, "drive/client/update.html", {"form": form, "id": id})


def traitementupdate(request, id):
    cform = ClientForm(request.POST)
    if cform.is_valid():
        client = cform.save(commit=False)
        client.id = id
        client.save()
        return HttpResponseRedirect("/drive/clients/")
    return render(request, "drive/client/update.html", {"form": cform, "id": id})
