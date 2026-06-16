# 🌱 Tableau de Bord Agricole du Togo

Projet réalisé dans le cadre du **Data Challenge Togo AI Lab — Défi 1**

## 📊 Objectif
Concevoir un tableau de bord interactif pour mieux comprendre la géographie
du tissu agricole au Togo.

## 🗂️ Structure du projet
togo-agri-dashboard/

├── data/                  # Données brutes et nettoyées

├── graphs/                # Graphiques Plotly

├── assets/                # Carte Folium

├── app.py                 # Dashboard Dash

├── map.py                 # Carte interactive

├── analyse.py             # Graphiques d'analyse

├── nettoyage.py           # Nettoyage des données

├── exploration.py         # Exploration des données

└── rapport.md             # Rapport final

## 🚀 Installation

```bash
git clone https://github.com/TON_USERNAME/togo-agri-dashboard.git
cd togo-agri-dashboard
python -m venv .venv
.venv\Scripts\activate
pip install pandas folium dash plotly
```

## ▶️ Lancer le dashboard

```bash
python app.py
```

Ouvre **http://127.0.0.1:8050** dans ton navigateur.

## 📦 Données
Données open data : [geodata.gouv.tg](https://geodata.gouv.tg) et
[opendata.gouv.tg](https://opendata.gouv.tg)

## 👤 Auteur
DJANFAROU Bilali — Togo AI Lab Data Challenge 2026