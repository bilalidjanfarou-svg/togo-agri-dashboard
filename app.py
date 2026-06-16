import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import folium
import os

# ---- Chargement des données ----
df_coop = pd.read_csv("data/cooperatives_clean.csv")
df_grandes = pd.read_csv("data/grandes_exploitations_clean.csv")
df_marches = pd.read_csv("data/marches_clean.csv")
df_plant = pd.read_csv("data/plantations_clean.csv")
df_zaaps = pd.read_csv("data/zaaps_clean.csv")
df_pep = pd.read_csv("data/pepinieres_clean.csv")

# ---- Application Dash ----
app = Dash(__name__)

app.layout = html.Div([

    # Titre
    html.H1("🌱 Tableau de Bord Agricole du Togo",
            style={"textAlign": "center", "color": "green"}),

    # Statistiques clés
    html.Div([
        html.Div([html.H3(len(df_coop)), html.P("Coopératives")], className="stat"),
        html.Div([html.H3(len(df_grandes)), html.P("Grandes Exploitations")], className="stat"),
        html.Div([html.H3(len(df_marches)), html.P("Marchés")], className="stat"),
        html.Div([html.H3(len(df_plant)), html.P("Plantations")], className="stat"),
        html.Div([html.H3(len(df_zaaps)), html.P("ZAAPs")], className="stat"),
        html.Div([html.H3(len(df_pep)), html.P("Pépinières")], className="stat"),
    ], style={"display": "flex", "justifyContent": "space-around", "margin": "20px"}),

    # Filtre par région
    html.Div([
        html.Label("Filtrer par région :"),
        dcc.Dropdown(
            id="filtre-region",
            options=[{"label": r, "value": r} for r in sorted(df_coop["region_nom_bdd"].dropna().unique())],
            value=None,
            placeholder="Toutes les régions",
            clearable=True
        )
    ], style={"width": "40%", "margin": "auto"}),

    # Graphiques
    html.Div([
        dcc.Graph(id="graph-coop"),
        dcc.Graph(id="graph-marches"),
    ], style={"display": "flex", "flexWrap": "wrap"}),

    html.Div([
        dcc.Graph(id="graph-terrain"),
        dcc.Graph(id="graph-annee"),
    ], style={"display": "flex", "flexWrap": "wrap"}),

    # Carte
    html.H2("🗺️ Carte Interactive", style={"textAlign": "center"}),
    html.Iframe(
        src="/assets/carte.html",
        style={"width": "100%", "height": "500px", "border": "none"}
    )
])

# ---- Callbacks ----
@app.callback(
    Output("graph-coop", "figure"),
    Output("graph-marches", "figure"),
    Output("graph-terrain", "figure"),
    Output("graph-annee", "figure"),
    Input("filtre-region", "value")
)
def update_graphs(region):
    coop = df_coop if not region else df_coop[df_coop["region_nom_bdd"] == region]
    marches = df_marches if not region else df_marches[df_marches["region_nom_bdd"] == region]
    plant = df_plant if not region else df_plant[df_plant["region_nom_bdd"] == region]
    grandes = df_grandes if not region else df_grandes[df_grandes["region_nom_bdd"] == region]

    fig1 = px.bar(coop.groupby("region_nom_bdd").size().reset_index(name="n"),
                  x="region_nom_bdd", y="n", title="Coopératives par région", color="region_nom_bdd")

    fig2 = px.bar(marches.groupby("region_nom_bdd").size().reset_index(name="n"),
                  x="region_nom_bdd", y="n", title="Marchés par région", color="region_nom_bdd")

    fig3 = px.pie(plant.groupby("terrain").size().reset_index(name="n"),
                  names="terrain", values="n", title="Plantations par terrain")

    fig4 = px.line(grandes.groupby("exploitation_annee").size().reset_index(name="n"),
                   x="exploitation_annee", y="n", title="Grandes exploitations par année")

    return fig1, fig2, fig3, fig4

if __name__ == "__main__":
    app.run(debug=True)