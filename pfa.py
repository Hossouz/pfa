import pandas as  pd
import numpy as  np
import os
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\yousbachi\OneDrive\Bureau\logiciel\PFA')

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

#Identifiez l’ID du produit ayant généré le plus gros bénéfice
best_product = df.loc[df['ca_net'].idxmax()]
print("----------Identifiez l’ID du produit ayant généré le plus gros bénéfice-------------")
print("ID du produit ayant généré le plus gros bénéfice :", best_product['ID'])

df.to_csv('resultats_final.csv', index=False)
print("resultats_final.csv ")


print(os.getcwd())
df.to_csv(r'C:\Users\yousbachi\OneDrive\Bureau\logiciel\PFA\resultats_final.csv', index=False)
print(" resultats_final.csv ")

print(os.getcwd())