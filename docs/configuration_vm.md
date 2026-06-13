# Configuration VM Linux

Ce fichier sert de trace pour la configuration des services sur la VM Linux.

## Objectif

La VM Linux heberge :

- le serveur MySQL ;
- l'application Django ;
- le service web permettant d'acceder au site depuis un navigateur.

## Paquets a installer

Exemple sur Debian/Ubuntu :

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv mysql-server git
```

Selon le choix du groupe, le service web peut etre :

```bash
sudo apt install apache2
```

ou :

```bash
sudo apt install nginx
```

## Recuperation du projet

```bash
git clone https://github.com/huymingbanchongphanith-arch/SAE203.git
cd SAE203
```

## Installation Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Creation de la base MySQL

```bash
sudo mysql < sae_drive_mysql.sql
```

Le fichier `Sae203/Sae203/settings.py` doit pointer vers la base `sae_drive`.

## Lancement de test

```bash
cd Sae203
python manage.py runserver 0.0.0.0:8000
```

Adresse de test depuis le navigateur :

```text
http://IP_DE_LA_VM:8000/drive/
```

## Exemple de service systemd

Fichier possible :

```text
/etc/systemd/system/sae203.service
```

Contenu d'exemple :

```ini
[Unit]
Description=Application Django SAE203
After=network.target mysql.service

[Service]
User=www-data
WorkingDirectory=/var/www/SAE203/Sae203
ExecStart=/var/www/SAE203/.venv/bin/python manage.py runserver 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Commandes :

```bash
sudo systemctl daemon-reload
sudo systemctl enable sae203
sudo systemctl start sae203
sudo systemctl status sae203
```

## Verification

- MySQL demarre correctement.
- La base `sae_drive` existe.
- Les tables sont creees.
- Le site est accessible depuis `http://IP_DE_LA_VM:8000/drive/`.
- Les CRUD fonctionnent.
- L'import CSV fonctionne avec le fichier `Sae203/drive/exemple_produits.csv`.
