from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .forms import CommandeForm
from . import models


def index(request):
    """Liste toutes les commandes avec le nom du client."""
    liste = list(models.Commande.objects.select_related("client").order_by("-date_commande"))
    return render(request, "drive/commande/index.html", {"liste": liste})


def ajout(request):
    """Affiche le formulaire de creation d'une commande.
    On affiche tous les clients et tous les produits avec un champ quantite.
    """
    form = CommandeForm()
    produits = models.Produit.objects.select_related("categorie").all().order_by("categorie__nom", "nom")
    return render(
        request,
        "drive/commande/ajout.html",
        {"form": form, "produits": produits},
    )


def traitement(request):
    """Traite la soumission du formulaire de creation de commande.
    Cree la commande puis les lignes de commande pour les produits dont la quantite > 0.
    """
    form = CommandeForm(request.POST)
    produit_ids = request.POST.getlist("produit_id")
    quantites = request.POST.getlist("quantite")

    # Verification : au moins un produit avec quantite > 0
    lignes_valides = [
        (pid, int(qte))
        for pid, qte in zip(produit_ids, quantites)
        if qte.isdigit() and int(qte) > 0
    ]

    if not form.is_valid() or not lignes_valides:
        produits = models.Produit.objects.select_related("categorie").all().order_by("categorie__nom", "nom")
        erreur = "Veuillez choisir un client et au moins un produit avec une quantite superieure a 0."
        return render(
            request,
            "drive/commande/ajout.html",
            {"form": form, "produits": produits, "erreur": erreur},
        )

    # Creation de la commande
    client = form.cleaned_data["client"]
    commande = models.Commande(client=client, date_commande=timezone.now())
    commande.save()

    # Creation des lignes de commande
    for pid, qte in lignes_valides:
        produit = models.Produit.objects.get(pk=pid)
        ligne = models.LigneCommande(commande=commande, produit=produit, quantite=qte)
        ligne.save()

    return HttpResponseRedirect("/drive/commandes/")


def affiche(request, id):
    """Affiche la fiche complete d'une commande avec le total."""
    commande = models.Commande.objects.select_related("client").get(pk=id)
    lignes = models.LigneCommande.objects.filter(commande=commande).select_related("produit__categorie")

    # Calcul du total de la commande
    total = sum(ligne.quantite * ligne.produit.prix for ligne in lignes)

    return render(
        request,
        "drive/commande/affiche.html",
        {"commande": commande, "lignes": lignes, "total": total},
    )


def delete(request, id):
    """Supprime une commande (et ses lignes par CASCADE)."""
    commande = models.Commande.objects.get(pk=id)
    commande.delete()
    return HttpResponseRedirect("/drive/commandes/")


def update(request, id):
    """Affiche le formulaire de modification d'une commande (changement de client)."""
    commande = models.Commande.objects.select_related("client").get(pk=id)
    form = CommandeForm(initial={"client": commande.client})
    lignes = models.LigneCommande.objects.filter(commande=commande).select_related("produit")
    produits = models.Produit.objects.select_related("categorie").all().order_by("categorie__nom", "nom")

    # Construire un dictionnaire produit_id -> quantite actuelle pour pre-remplir
    quantites_actuelles = {str(l.produit_id): l.quantite for l in lignes}

    return render(
        request,
        "drive/commande/update.html",
        {
            "commande": commande,
            "form": form,
            "produits": produits,
            "quantites_actuelles": quantites_actuelles,
        },
    )


def traitementupdate(request, id):
    """Traite la modification d'une commande : recrée toutes les lignes."""
    form = CommandeForm(request.POST)
    produit_ids = request.POST.getlist("produit_id")
    quantites = request.POST.getlist("quantite")

    lignes_valides = [
        (pid, int(qte))
        for pid, qte in zip(produit_ids, quantites)
        if qte.isdigit() and int(qte) > 0
    ]

    if not form.is_valid() or not lignes_valides:
        return HttpResponseRedirect(f"/drive/updatecommande/{id}/")

    # Mise a jour de la commande
    commande = models.Commande.objects.get(pk=id)
    commande.client = form.cleaned_data["client"]
    commande.save()

    # Suppression des anciennes lignes et recreation
    models.LigneCommande.objects.filter(commande=commande).delete()
    for pid, qte in lignes_valides:
        produit = models.Produit.objects.get(pk=pid)
        models.LigneCommande(commande=commande, produit=produit, quantite=qte).save()

    return HttpResponseRedirect("/drive/commandes/")
