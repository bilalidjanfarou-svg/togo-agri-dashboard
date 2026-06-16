import pandas as pd
import re

def extraire_coords(geometry):
    try:
        coords = re.findall(r'[-\d.]+', geometry)
        lon, lat = float(coords[0]), float(coords[1])
        return lat, lon
    except:
        return None, None

fichiers = {
    "cooperatives": "data/cooperatives.csv",
    "grandes_exploitations": "data/grandes_exploitations.csv",
    "marches": "data/marches.csv",
    "pepinieres": "data/pepinieres.csv",
    "petites_exploitations": "data/petites_exploitations.csv",
    "plantations": "data/plantations.csv",
    "zaaps": "data/zaaps.csv",
}

for nom, chemin in fichiers.items():
    try:
        df = pd.read_csv(chemin, on_bad_lines='skip')
        
        df[['latitude', 'longitude']] = df['geometry'].apply(
            lambda g: pd.Series(extraire_coords(str(g)))
        )
        
        df = df.dropna(subset=['latitude', 'longitude'])
        df.to_csv(f"data/{nom}_clean.csv", index=False)
        print(f"✅ {nom} : {len(df)} lignes nettoyées")
        
    except Exception as e:
        print(f"❌ {nom} : erreur -> {e}")


