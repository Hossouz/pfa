import pandas as  pd
import numpy as  np
import os
import matplotlib.pyplot as plt


#generate vente.csv file----------------------------------------------------------

NB_PRODUITS = int(input("Entrez le nombre de produits à générer : "))

# =========================
# GENERATION ALEATOIRE
# =========================
data = {
    'ID': range(101, 101 + NB_PRODUITS),
    'prix': np.random.uniform(5, 600, NB_PRODUITS).round(2),
    'quantite': np.random.randint(1, 20, NB_PRODUITS),
    'remise': np.random.choice([0, 5, 10, 15, 20], NB_PRODUITS)
}
df = pd.DataFrame(data)
df.to_csv('ventes.csv', index=False)
df = pd.read_csv('ventes.csv')

print(df.head(len(df)))
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

''''''
print(os.getcwd())



print(df.columns)

plt.figure(figsize=(20, 6))
plt.plot(df['ID'], df['ca_net'], color='hotpink', linewidth=1)
plt.fill_between(df['ID'], df['ca_net'], alpha=0.3, color='pink')  
plt.title('CA Net par Produit', fontsize=16)
plt.xlabel('ID Produit', fontsize=12)
plt.ylabel('CA Net (TND)', fontsize=12)
plt.xticks(fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('graphique_CA.png', dpi=300)
os.startfile('graphique_CA.png')