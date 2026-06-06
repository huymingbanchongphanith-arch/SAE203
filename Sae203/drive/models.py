from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    descriptif = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "categorie"

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom": self.nom, "descriptif": self.descriptif}


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    date_peremption = models.DateField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    marque = models.CharField(max_length=100, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.RESTRICT)

    class Meta:
        db_table = "produit"

    def __str__(self):
        return f"{self.nom} - {self.prix} euros"

    def dico(self):
        return {
            "nom": self.nom,
            "date_peremption": self.date_peremption,
            "photo": self.photo,
            "marque": self.marque,
            "prix": self.prix,
            "categorie": self.categorie,
        }


class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField()
    adresse = models.CharField(max_length=255)

    class Meta:
        db_table = "client"

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Commande(models.Model):
    numero = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    date_commande = models.DateTimeField()

    class Meta:
        db_table = "commande"

    def __str__(self):
        return f"Commande numero {self.numero}"


class LigneCommande(models.Model):
    pk = models.CompositePrimaryKey("commande", "produit")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, db_column="commande_numero")
    produit = models.ForeignKey(Produit, on_delete=models.RESTRICT)
    quantite = models.IntegerField()

    class Meta:
        db_table = "ligne_commande"

    def __str__(self):
        return f"{self.produit} x {self.quantite}"
