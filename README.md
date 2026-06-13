# SAE203 - Application de gestion d'un Drive

Projet realise dans le cadre de la SAE203 / competence RT3 informatique.

L'objectif est de fournir une interface web de gestion d'un Drive. L'application permet de consulter, ajouter, modifier et supprimer des categories, des produits, des clients et des commandes. Elle utilise une base de donnees MySQL et une application web Django.

## Fonctionnalites

- Accueil avec navigation vers les differents modules.
- CRUD categories.
- CRUD produits.
- Import de produits depuis un fichier CSV.
- CRUD clients.
- CRUD commandes.
- Gestion des quantites de produits dans une commande.
- Fiche commande avec liste des produits et total de la commande.
- Schema relationnel et script SQL fournis dans le depot.

## Technologies utilisees

- Python 3
- Django
- MySQL
- HTML / CSS
- Git et GitHub
- VM Linux pour le deploiement final

## Structure du depot

```text
SAE203/
├── README.md
├── requirements.txt
├── sae_drive_mysql.sql
├── schema_drive.html
├── docs/
│   ├── fiche_procedure_sae_drive.md
│   ├── fiche_procedure_sae_drive.docx
│   ├── gantt_sae_drive.md
│   ├── schema_drive_mermaid.mmd
│   └── configuration_vm.md
└── Sae203/
    ├── manage.py
    ├── Sae203/
    │   └── settings.py
    └── drive/
        ├── models.py
        ├── forms.py
        ├── categorie_views.py
        ├── produit_views.py
        ├── client_views.py
        ├── commande_views.py
        ├── urls.py
        ├── templates/
        └── static/
```

## Base de donnees

La base de donnees s'appelle `sae_drive`.

Le script SQL principal est :

```text
sae_drive_mysql.sql
```

Il contient :

- la creation de la base ;
- les tables `categorie`, `produit`, `client`, `commande`, `ligne_commande` ;
- les cles primaires et cles etrangeres ;
- les contraintes de verification ;
- des donnees de test ;
- quelques requetes utiles pour verifier la base.

Le schema relationnel est disponible dans :

```text
schema_drive.html
docs/schema_drive_mermaid.mmd
```

## Installation rapide

Installer les dependances Python :

```powershell
pip install -r requirements.txt
```

Importer la base MySQL :

```powershell
mysql -u root < sae_drive_mysql.sql
```

Lancer le serveur Django :

```powershell
cd Sae203
python manage.py runserver 127.0.0.1:8000
```

Adresse de test :

```text
http://127.0.0.1:8000/drive/
```

## Repartition des taches

| Etudiant | Partie principale |
| --- | --- |
| Etudiant 1 | Base de donnees, schema SQL, creation des tables, donnees de test, CRUD categories/produits, import CSV |
| Etudiant 2 | Infrastructure Linux, VM, service web, PHP/MySQL ou configuration serveur, CRUD clients, validation formulaires |
| Etudiant 3 | Application web, structure du site, navigation, CRUD commandes, gestion des quantites, fiche commande |

## Documents de rendu

Les documents utiles au rendu sont dans le dossier `docs/` :

- `fiche_procedure_sae_drive.md` : fiche de procedure au format texte.
- `fiche_procedure_sae_drive.docx` : fiche de procedure au format Word.
- `gantt_sae_drive.md` : planning et diagramme de Gantt.
- `schema_drive_mermaid.mmd` : schema relationnel en Mermaid.
- `configuration_vm.md` : aide de configuration pour la VM Linux.

## Commandes utiles Git

```powershell
git status
git add .
git commit -m "Message du commit"
git push origin main
```
