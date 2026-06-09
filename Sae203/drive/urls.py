from django.urls import path
from . import categorie_views, produit_views, views

urlpatterns = [
    path("", views.index),
    path("categories/", categorie_views.index),
    path("ajoutcategorie/", categorie_views.ajout),
    path("traitementcategorie/", categorie_views.traitement),
    path("affichecategorie/<int:id>/", categorie_views.affiche),
    path("deletecategorie/<int:id>/", categorie_views.delete),
    path("updatecategorie/<int:id>/", categorie_views.update),
    path("traitementupdatecategorie/<int:id>/", categorie_views.traitementupdate),
    path("produits/", produit_views.index),
    path("ajoutproduit/", produit_views.ajout),
    path("traitementproduit/", produit_views.traitement),
    path("afficheproduit/<int:id>/", produit_views.affiche),
    path("deleteproduit/<int:id>/", produit_views.delete),
    path("updateproduit/<int:id>/", produit_views.update),
    path("traitementupdateproduit/<int:id>/", produit_views.traitementupdate),
    path("importproduitscsv/", produit_views.import_csv),
    path("traitementimportproduitscsv/", produit_views.traitement_import_csv),

    #commandes
    path("commandes/", commande_views.index),
    path("ajoutcommande/", commande_views.ajout),
    path("traitementcommande/", commande_views.traitement),
    path("affichecommande/<int:id>/", commande_views.affiche),
    path("deletecommande/<int:id>/", commande_views.delete),
    path("updatecommande/<int:id>/", commande_views.update),
    path("traitementupdatecommande/<int:id>/", commande_views.traitementupdate),
]
