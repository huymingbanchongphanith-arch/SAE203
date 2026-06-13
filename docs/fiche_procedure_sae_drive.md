# Fiche de procedure - SAE203 Drive

## 1. Presentation du projet

Le projet consiste a creer une application web de gestion d'un Drive. Le site permet de gerer des categories de produits, des produits, des clients et des commandes. Les clients peuvent passer des commandes contenant plusieurs produits avec une quantite pour chaque produit.

Cette application valide les apprentissages lies a l'utilisation d'un systeme informatique, a la modification d'un programme, au developpement web, a la gestion de donnees et au travail collaboratif.

## 2. Infrastructure mise en place

L'application est prevue pour etre deployee sur une machine virtuelle Linux. Cette VM contient les services necessaires au fonctionnement du projet :

- un serveur MySQL pour stocker les donnees ;
- Python et Django pour l'application web ;
- un service web ou un lancement Django pour rendre le site accessible ;
- Git pour recuperer le depot du projet.

En developpement local, le site peut aussi etre teste avec le serveur integre de Django.

## 3. Technologies utilisees

| Element | Technologie |
| --- | --- |
| Application web | Django |
| Langage serveur | Python |
| Base de donnees | MySQL |
| Interface | HTML / CSS |
| Versionnement | Git / GitHub |
| Deploiement | VM Linux |

## 4. Structure de la base de donnees

La base de donnees s'appelle `sae_drive`.

Elle contient cinq tables principales :

- `categorie` : stocke les categories de produits ;
- `produit` : stocke les produits disponibles dans le Drive ;
- `client` : stocke les clients ;
- `commande` : stocke les commandes passees par les clients ;
- `ligne_commande` : stocke les produits contenus dans une commande avec leur quantite.

La table `ligne_commande` est une table de liaison entre `commande` et `produit`. Elle permet de representer le fait qu'une commande peut contenir plusieurs produits et qu'un produit peut etre present dans plusieurs commandes.

Le script SQL de creation et de remplissage se trouve dans :

```text
sae_drive_mysql.sql
```

Le schema relationnel se trouve dans :

```text
schema_drive.html
docs/schema_drive_mermaid.mmd
```

## 5. Fonctionnement de l'application

Le projet Django contient une application nommee `drive`.

Les modeles Django dans `models.py` representent les tables MySQL. Chaque modele correspond a une table :

- `Categorie` correspond a la table `categorie` ;
- `Produit` correspond a la table `produit` ;
- `Client` correspond a la table `client` ;
- `Commande` correspond a la table `commande` ;
- `LigneCommande` correspond a la table `ligne_commande`.

Les formulaires dans `forms.py` permettent de saisir et verifier les donnees envoyees par l'utilisateur. Les vues se trouvent dans plusieurs fichiers pour mieux separer le code :

- `categorie_views.py` pour les categories ;
- `produit_views.py` pour les produits et l'import CSV ;
- `client_views.py` pour les clients ;
- `commande_views.py` pour les commandes.

Le fichier `urls.py` relie les adresses du site aux fonctions Python correspondantes.

## 6. Installation de la base MySQL

Sur la VM Linux ou sur le poste de developpement, il faut installer MySQL puis importer le script :

```bash
mysql -u root < sae_drive_mysql.sql
```

Ce script supprime l'ancienne base si elle existe, recree la base `sae_drive`, cree les tables, ajoute les contraintes et insere les donnees de test.

En production, il faudrait eviter de supprimer la base automatiquement, mais pour une SAE et une demonstration, cela permet de repartir d'une base propre.

## 7. Configuration Django

La connexion entre Django et MySQL est configuree dans :

```text
Sae203/Sae203/settings.py
```

Configuration utilisee :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sae_drive',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Cette configuration indique a Django d'utiliser le moteur MySQL et la base `sae_drive`.

## 8. Installation de l'application

Recuperer le projet :

```bash
git clone https://github.com/huymingbanchongphanith-arch/SAE203.git
cd SAE203
```

Installer les dependances :

```bash
pip install -r requirements.txt
```

Aller dans le dossier Django :

```bash
cd Sae203
```

Verifier que le projet ne contient pas d'erreur Django :

```bash
python manage.py check
```

## 9. Lancement du site

En local :

```bash
python manage.py runserver 127.0.0.1:8000
```

Sur la VM Linux :

```bash
python manage.py runserver 0.0.0.0:8000
```

Adresse de test :

```text
http://127.0.0.1:8000/drive/
```

ou, sur la VM :

```text
http://IP_DE_LA_VM:8000/drive/
```

## 10. Tests a effectuer

Avant le rendu, les tests suivants doivent etre realises :

- ouvrir la page d'accueil ;
- afficher la liste des categories ;
- ajouter, modifier et supprimer une categorie ;
- afficher la liste des produits ;
- ajouter, modifier et supprimer un produit ;
- importer un fichier CSV de produits ;
- afficher la liste des clients ;
- ajouter, modifier et supprimer un client ;
- creer une commande avec plusieurs produits ;
- modifier une commande ;
- afficher une fiche commande avec le total ;
- verifier que la base MySQL contient bien les donnees.

## 11. Repartition des taches

| Etudiant | Taches principales |
| --- | --- |
| Etudiant 1 | Base de donnees, schema SQL, tables, donnees de test, CRUD categories, CRUD produits, import CSV |
| Etudiant 2 | VM Linux, installation des services, configuration MySQL, CRUD clients, validation formulaires |
| Etudiant 3 | Structure du site, navigation, CRUD commandes, gestion des quantites, fiche commande avec total |

## 12. Conclusion

Le projet permet de manipuler une base de donnees MySQL depuis une interface web Django. Il repond au besoin d'un Drive en proposant une gestion des produits, des clients et des commandes. Le depot GitHub contient le code de l'application, le script SQL, le schema relationnel, le planning et la documentation de deploiement.
