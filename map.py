import pandas as pd
import folium

print("Démarrage...")

try:
    carte = folium.Map(location=[8.6195, 0.8248], zoom_start=7)
    print("✅ Carte créée")

    couches = {
        "Coopératives": ("data/cooperatives_clean.csv", "blue", "cooperative_nom"),
        "Grandes Exploitations": ("data/grandes_exploitations_clean.csv", "red", "exploitation_nom"),
        "Marchés": ("data/marches_clean.csv", "green", "marche_nom"),
        "Pépinières": ("data/pepinieres_clean.csv", "orange", "etab_nom"),
        "Plantations": ("data/plantations_clean.csv", "purple", "exploitation_nom"),
        "ZAAPs": ("data/zaaps_clean.csv", "darkred", "cooperative_nom"),
    }

    for nom_couche, (chemin, couleur, col_nom) in couches.items():
        print(f"Chargement {nom_couche}...")
        groupe = folium.FeatureGroup(name=nom_couche)
        df = pd.read_csv(chemin)
        print(f"  -> {len(df)} lignes")

        for _, row in df.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=4,
                color=couleur,
                fill=True,
                fill_opacity=0.7,
                popup=str(row.get(col_nom, '')) + f" ({row.get('region_nom_bdd', '')})"
            ).add_to(groupe)

        groupe.add_to(carte)
        print(f"✅ {nom_couche} ajouté")

    folium.LayerControl().add_to(carte)
    carte.save("carte_agricole_togo.html")
    print("✅ Carte sauvegardée !")

except Exception as e:
    print(f"❌ Erreur : {e}")