import pandas as pd
import os

dossier = "data/"
fichiers = os.listdir(dossier)
print(f"Fichiers trouvés : {fichiers}")

for fichier in fichiers:
    if fichier.endswith(".csv"):
        print(f"\n{'='*40}")
        print(f"📄 {fichier}")
        print('='*40)
        
        df = pd.read_csv(dossier + fichier, encoding='utf-8', on_bad_lines='skip')
        
        print(f"Lignes : {df.shape[0]} | Colonnes : {df.shape[1]}")
        print(f"\nColonnes : {list(df.columns)}")
        print(f"\nAperçu :")
        print(df.head(3))
        