-- Base de donnees pour la SAE : gestion d'un Drive
-- Script MySQL complet : creation, tables, contraintes et donnees de test

DROP DATABASE IF EXISTS sae_drive;
CREATE DATABASE sae_drive
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE sae_drive;

-- ============================================================
-- Table des categories de produits
-- ============================================================
CREATE TABLE categorie (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  descriptif TEXT,
  CONSTRAINT uk_categorie_nom UNIQUE (nom)
) ENGINE=InnoDB;

-- ============================================================
-- Table des produits
-- Un produit appartient a une seule categorie.
-- ============================================================
CREATE TABLE produit (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(150) NOT NULL,
  date_peremption DATE,
  photo VARCHAR(255),
  marque VARCHAR(100),
  prix DECIMAL(10,2) NOT NULL,
  categorie_id INT NOT NULL,

  CONSTRAINT chk_produit_prix CHECK (prix >= 0),
  CONSTRAINT fk_produit_categorie
    FOREIGN KEY (categorie_id)
    REFERENCES categorie(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ============================================================
-- Table des clients
-- Un client peut passer plusieurs commandes.
-- ============================================================
CREATE TABLE client (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  prenom VARCHAR(100) NOT NULL,
  date_inscription DATE NOT NULL DEFAULT (CURRENT_DATE),
  adresse VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

-- ============================================================
-- Table des commandes
-- Une commande appartient a un seul client.
-- ============================================================
CREATE TABLE commande (
  numero INT AUTO_INCREMENT PRIMARY KEY,
  client_id INT NOT NULL,
  date_commande DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_commande_client
    FOREIGN KEY (client_id)
    REFERENCES client(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ============================================================
-- Table de liaison entre commande et produit
-- Elle contient la quantite de chaque produit commande.
-- Cle primaire composee : un meme produit ne peut apparaitre
-- qu'une seule fois dans une meme commande.
-- ============================================================
CREATE TABLE ligne_commande (
  commande_numero INT NOT NULL,
  produit_id INT NOT NULL,
  quantite INT NOT NULL,

  PRIMARY KEY (commande_numero, produit_id),

  CONSTRAINT chk_ligne_commande_quantite CHECK (quantite > 0),
  CONSTRAINT fk_ligne_commande_commande
    FOREIGN KEY (commande_numero)
    REFERENCES commande(numero)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_ligne_commande_produit
    FOREIGN KEY (produit_id)
    REFERENCES produit(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ============================================================
-- Donnees de test : categories
-- ============================================================
INSERT INTO categorie (nom, descriptif) VALUES
('Fruits et legumes', 'Produits frais : fruits et legumes de saison'),
('Boissons', 'Eaux, jus, sodas et boissons diverses'),
('Epicerie', 'Produits alimentaires non frais'),
('Produits laitiers', 'Lait, yaourts, fromages et desserts lactes'),
('Hygiene', 'Produits d hygiene et de soin');

-- ============================================================
-- Donnees de test : produits
-- ============================================================
INSERT INTO produit (nom, date_peremption, photo, marque, prix, categorie_id) VALUES
('Pommes Golden 1kg', '2026-07-15', 'pommes_golden.jpg', 'Vergers du Sud', 2.49, 1),
('Bananes 1kg', '2026-07-10', 'bananes.jpg', 'Tropic Fruit', 1.99, 1),
('Carottes 1kg', '2026-07-20', 'carottes.jpg', 'Primeur Bio', 1.75, 1),
('Eau minerale 6x1.5L', '2027-01-30', 'eau_minerale.jpg', 'Cristaline', 3.20, 2),
('Jus orange 1L', '2026-10-05', 'jus_orange.jpg', 'Tropicana', 2.10, 2),
('Pates spaghetti 500g', '2027-12-01', 'spaghetti.jpg', 'Barilla', 1.35, 3),
('Riz basmati 1kg', '2028-03-12', 'riz_basmati.jpg', 'Taureau Aile', 3.80, 3),
('Lait demi-ecreme 1L', '2026-08-05', 'lait.jpg', 'Candia', 1.15, 4),
('Yaourts nature x4', '2026-07-25', 'yaourts.jpg', 'Danone', 2.30, 4),
('Dentifrice menthe', NULL, 'dentifrice.jpg', 'Signal', 2.85, 5);

-- ============================================================
-- Donnees de test : clients
-- ============================================================
INSERT INTO client (nom, prenom, date_inscription, adresse) VALUES
('Dupont', 'Marie', '2026-05-10', '12 rue des Lilas, 59000 Lille'),
('Martin', 'Lucas', '2026-05-12', '8 avenue Victor Hugo, 62000 Arras'),
('Bernard', 'Emma', '2026-05-18', '25 boulevard Carnot, 80000 Amiens');

-- ============================================================
-- Donnees de test : commandes et lignes de commande
-- ============================================================
INSERT INTO commande (client_id, date_commande) VALUES
(1, '2026-06-01 10:30:00'),
(2, '2026-06-02 15:45:00'),
(1, '2026-06-03 09:15:00');

INSERT INTO ligne_commande (commande_numero, produit_id, quantite) VALUES
(1, 1, 2),
(1, 4, 1),
(1, 8, 3),
(2, 6, 2),
(2, 7, 1),
(2, 9, 2),
(3, 2, 1),
(3, 5, 2),
(3, 10, 1);

-- ============================================================
-- Requetes utiles pour le projet
-- ============================================================

-- Liste des produits avec leur categorie
SELECT
  p.id,
  p.nom,
  p.marque,
  p.prix,
  p.date_peremption,
  c.nom AS categorie
FROM produit p
JOIN categorie c ON c.id = p.categorie_id
ORDER BY c.nom, p.nom;

-- Fiche detaillee d'une commande, ici la commande numero 1
SELECT
  co.numero AS numero_commande,
  co.date_commande,
  cl.nom AS client_nom,
  cl.prenom AS client_prenom,
  cl.adresse,
  p.nom AS produit,
  p.marque,
  lc.quantite,
  p.prix AS prix_unitaire,
  lc.quantite * p.prix AS total_ligne
FROM commande co
JOIN client cl ON cl.id = co.client_id
JOIN ligne_commande lc ON lc.commande_numero = co.numero
JOIN produit p ON p.id = lc.produit_id
WHERE co.numero = 1;

-- Total d'une commande, ici la commande numero 1
SELECT
  co.numero AS numero_commande,
  CONCAT(cl.prenom, ' ', cl.nom) AS client,
  SUM(lc.quantite * p.prix) AS total_commande
FROM commande co
JOIN client cl ON cl.id = co.client_id
JOIN ligne_commande lc ON lc.commande_numero = co.numero
JOIN produit p ON p.id = lc.produit_id
WHERE co.numero = 1
GROUP BY co.numero, cl.prenom, cl.nom;

-- Nombre de commandes par client
SELECT
  cl.id,
  cl.nom,
  cl.prenom,
  COUNT(co.numero) AS nombre_commandes
FROM client cl
LEFT JOIN commande co ON co.client_id = cl.id
GROUP BY cl.id, cl.nom, cl.prenom
ORDER BY cl.nom, cl.prenom;

