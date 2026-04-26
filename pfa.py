import pandas as  pd
import numpy as  np


#generate vente.csv file----------------------------------------------------------
data = {
    'ID'       : range(101, 151),
    'prix'     : np.random.uniform(5, 600, 50).round(2),
    'quantite' : np.random.randint(1, 20, 50),
    'remise'   : np.random.choice([0, 5, 10, 15, 20], 50)
}
df = pd.DataFrame(data)
df.to_csv('ventes.csv', index=False)
df = pd.read_csv('ventes.csv')
print(df.head())
#Calcule de Chiffre d’Affaires Brut (Prix × Quantité) pour chaque ligne.
df["Chiffre d'affaires Brut"] = df["prix"] * df["quantite"]
print("----------Calcule de Chiffre d’Affaires Brut (Prix × Quantité) pour chaque ligne.-------------")
print(df.head())

#Appliquez les remises (en pourcentage) pour obtenir le CA Net.
df["ca_net"] = df["prix"] *df["quantite"] * (1-df["remise"]/100)
print("----------Appliquez les remises (en pourcentage) pour obtenir le CA Net.-------------")
print(df[['prix','quantite','remise','ca_net']].head())

#calcule de tva sur le ca net 
df["tva"] = df["ca_net"] * 0.2
print("----------calcule de tva sur le ca net -------------")
print(df[['ca_net','tva']].head())
#affichage de  CA_TOTAL
ca_total = df["ca_net"].sum()
print("----------CA TOTAL-------------")
print("CA TOTAL :", ca_total)
