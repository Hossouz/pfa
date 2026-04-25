import pandas as  pd
import numpy as  np

df = pd.read_csv(r"C:\logiciel\PFA\archive\Updated_sales.csv")
print(df.head())

print(df.info() ) 
df["discount"] = np.random.choice([0, 5, 10, 15, 20], size=len(df))
print(df.head())
print(df.describe())
print(df.info())
df = df.rename(columns={ "Order ID": "ID", 
                         "Product": "produit", 
                         "Price Each": "prix", 
                         "Quantity Ordered": "quantite", 
                         "Order Date": "order_date", 
                         "Customer ID": "customer_ID", 
                         "discount": "remise"   })
print(df.columns)

print(df.head())
df = df.dropna()
print(df.head())
print("-----------------------------------------------------------------------")
print(df.dtypes)
df["quantite"] = pd.to_numeric(df["quantite"], errors="coerce")
df["prix"] = pd.to_numeric(df["prix"], errors="coerce")
print("-----------------------------------------------------------------------")
print(df.dtypes)

#Calcule de Chiffre d’Affaires Brut (Prix × Quantité) pour chaque ligne.
df["Chiffre d'affaires Brut"] = df["prix"] * df["quantite"]
print(df.head())

#Appliquez les remises (en pourcentage) pour obtenir le CA Net.
df["ca_net"] = df["prix"] *df["quantite"] * (1-df["remise"]/100)
print(df[['prix','quantite','remise','ca_net']].head())

#calcule de tva sur le ca net 
df["tva"] = df["ca_net"] * 0.2
print(df[['ca_net','tva']].head())
ca_total = df["ca_net"].sum()
print("CA TOTAL :", ca_total)