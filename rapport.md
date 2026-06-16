# Rapport — Data Challenge Agriculture Togo
**Togo AI Lab | Défi 1 | Juin 2026**

---

## 1. Introduction

Ce projet a été réalisé dans le cadre du Data Challenge mensuel du Togo AI Lab.
L'objectif est de concevoir un tableau de bord interactif pour mieux comprendre
la géographie du tissu agricole au Togo.

---

## 2. Sources de données

Les données proviennent des plateformes open data du gouvernement togolais :
- **geodata.gouv.tg** et **opendata.gouv.tg**

| Fichier | Lignes |
|---|---|
| Coopératives Agricoles | 6 859 |
| Grandes Exploitations | 220 |
| Marchés | 1 078 |
| Pépinières | 728 |
| Petites Exploitations | 13 119 |
| Plantations | 2 911 |
| ZAAPs/ZAPBs | 1 883 |

---

## 3. Méthodologie

### 3.1 Nettoyage des données
- Extraction des coordonnées GPS depuis la colonne `geometry`
- Suppression des lignes sans coordonnées valides
- Renommage des fichiers pour faciliter le traitement

### 3.2 Outils utilisés
- **Python** : langage principal
- **Pandas** : nettoyage et analyse des données
- **Folium** : carte interactive
- **Plotly** : graphiques d'analyse
- **Dash** : tableau de bord interactif

---

## 4. Analyses et Résultats

### 4.1 Densité des coopératives par région
La région Maritime concentre le plus grand nombre de coopératives agricoles,
suivie de la région des Plateaux.

### 4.2 Couverture des ZAAPs
Les Zones d'Aménagement Agricole Planifiées (ZAAPs) sont principalement
concentrées dans les régions des Plateaux et Centrale.

### 4.3 Accessibilité aux marchés
La région Maritime dispose du plus grand nombre de marchés agricoles,
ce qui facilite l'accès aux services pour les agriculteurs.

### 4.4 Réseau coopératif
Avec 6 859 coopératives recensées, le réseau coopératif togolais est dense,
bien que inégalement réparti entre les régions.

---

## 5. Conclusion

Ce tableau de bord permet de visualiser et d'analyser la géographie agricole
du Togo de manière interactive. Il met en évidence les disparités régionales
et peut aider les décideurs à mieux orienter les politiques agricoles.

---

## 6. Livrables

- `app.py` — Dashboard interactif Dash
- `carte_agricole_togo.html` — Carte interactive Folium
- `graphs/` — Graphiques d'analyse Plotly
- `rapport.md` — Ce rapport

---

*Réalisé avec Python | Données : geodata.gouv.tg & opendata.gouv.tg*