# Planning du projet SAE203

Ce planning resume la repartition des taches du projet de gestion d'un Drive.

```mermaid
gantt
    title Planning SAE203 - Gestion d'un Drive
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m

    section Etudiant 1 - Base de donnees
    Analyse du schema de donnees              :done, e1a, 2026-05-20, 1d
    Creation du script SQL                    :done, e1b, after e1a, 2d
    Donnees de test                           :done, e1c, after e1b, 1d
    CRUD categories et produits               :done, e1d, 2026-05-26, 3d
    Import produits CSV                       :done, e1e, after e1d, 2d

    section Etudiant 2 - Infrastructure et clients
    Preparation de la VM Linux                :done, e2a, 2026-05-20, 2d
    Installation des services                 :done, e2b, after e2a, 2d
    Connexion MySQL / application             :done, e2c, 2026-05-26, 2d
    CRUD clients                              :done, e2d, after e2c, 2d
    Validation des formulaires                :done, e2e, after e2d, 1d

    section Etudiant 3 - Application web
    Structure du site                         :done, e3a, 2026-05-20, 2d
    Navigation et templates                   :done, e3b, after e3a, 2d
    CRUD commandes                            :done, e3c, 2026-05-26, 3d
    Gestion des quantites                     :done, e3d, after e3c, 2d
    Fiche commande et total                   :done, e3e, after e3d, 1d

    section Groupe
    Tests et corrections                      :done, g1, 2026-06-04, 3d
    Documentation et procedure                :done, g2, after g1, 2d
    Preparation presentation                  :done, g3, after g2, 1d
```

## Tableau de repartition

| Etudiant | Responsabilites |
| --- | --- |
| Etudiant 1 | Base SQL, schema relationnel, tables, donnees de test, CRUD categories, CRUD produits, import CSV |
| Etudiant 2 | VM Linux, installation des services, configuration MySQL, CRUD clients, validation des formulaires |
| Etudiant 3 | Structure web, navigation, CRUD commandes, lignes de commande, calcul du total |
