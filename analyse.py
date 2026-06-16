import pandas as pd
import plotly.express as px

print("Démarrage...")

try:
    # ---- 1. Densité des coopératives par région ----
    df_coop = pd.read_csv("data/cooperatives_clean.csv")
    coop_region = df_coop.groupby("region_nom_bdd").size().reset_index(name="nombre")

    fig1 = px.bar(
        coop_region,
        x="region_nom_bdd",
        y="nombre",
        title="Nombre de coopératives par région",
        color="region_nom_bdd",
        labels={"region_nom_bdd": "Région", "nombre": "Nombre"}
    )
    fig1.write_html("graphs/cooperatives_par_region.html")
    print("✅ Graphique 1 : coopératives par région")

    # ---- 2. Plantations par type de terrain ----
    df_plant = pd.read_csv("data/plantations_clean.csv")
    plant_terrain = df_plant.groupby("terrain").size().reset_index(name="nombre")

    fig2 = px.pie(
        plant_terrain,
        names="terrain",
        values="nombre",
        title="Plantations par type de terrain"
    )
    fig2.write_html("graphs/plantations_par_terrain.html")
    print("✅ Graphique 2 : plantations par terrain")

    # ---- 3. Marchés par région ----
    df_march = pd.read_csv("data/marches_clean.csv")
    march_region = df_march.groupby("region_nom_bdd").size().reset_index(name="nombre")

    fig3 = px.bar(
        march_region,
        x="region_nom_bdd",
        y="nombre",
        title="Nombre de marchés par région",
        color="region_nom_bdd",
        labels={"region_nom_bdd": "Région", "nombre": "Nombre"}
    )
    fig3.write_html("graphs/marches_par_region.html")
    print("✅ Graphique 3 : marchés par région")

    # ---- 4. Grandes exploitations par année ----
    df_grandes = pd.read_csv("data/grandes_exploitations_clean.csv")
    grandes_annee = df_grandes.groupby("exploitation_annee").size().reset_index(name="nombre")

    fig4 = px.line(
        grandes_annee,
        x="exploitation_annee",
        y="nombre",
        title="Création de grandes exploitations par année",
        labels={"exploitation_annee": "Année", "nombre": "Nombre"}
    )
    fig4.write_html("graphs/grandes_exploitations_par_annee.html")
    print("✅ Graphique 4 : grandes exploitations par année")

except Exception as e:
    print(f"❌ Erreur : {e}")