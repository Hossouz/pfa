# pfa
Automatisation des Ventes , Python script that automates e-commerce sales analysis  reads CSV data, calculates revenue (CA Brut, CA Net), applies discounts, computes TVA (20%), identifies the best-selling product, and exports results. Built with Pandas &amp; Matplotlib
# 📊 Analyse des ventes – Python


---

## 📌 Description

Ce projet a pour objectif d’automatiser l’analyse des ventes d’une entreprise de e-commerce à partir d’un fichier CSV.

Face à l’augmentation du volume de données, l’utilisation d’un tableur classique devient limitée. Ce script Python permet de :

* Lire un fichier de ventes
* Effectuer des calculs financiers
* Générer des indicateurs clés
* Exporter les résultats dans un nouveau fichier

---

## 🎯 Fonctionnalités

✔️ Lecture d’un fichier CSV (`ventes.csv`)
✔️ Calcul du **Chiffre d’Affaires Brut (CA Brut)**
✔️ Application des **remises (%)**
✔️ Calcul du **Chiffre d’Affaires Net (CA Net)**
✔️ Calcul de la **TVA (20%)**
✔️ Calcul du **CA total de l’entreprise**
✔️ Identification du **produit le plus rentable**
✔️ Export des résultats vers `resultats_final.csv`

---

## 📂 Structure du projet

```id="projstruct"
analyse_ventes/
│
├── pfa.py
├── ventes.csv
├── resultats_final.csv
├── graphique_CA.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Prérequis

* Python 3.x
* VS Code 

### (Optionnel)

* matplotlib pour les graphiques

```bash id="installmatplotlib"
pip install matplotlib
```

---

## 📥 Installation

1. Cloner le dépôt ou télécharger le projet
2. Placer le fichier `ventes.csv` dans le dossier
3. Ouvrir le projet dans VS Code

---

## ▶️ Utilisation

### 1. Format du fichier d'entrée

Le fichier `ventes.csv` doit respecter le format suivant :

```id="formatcsv"
id,prix,quantite,remise
101,599.99,3,10
102,49.99,2,5
103,19.99,5,0
```

---

### 2. Exécution

Dans le terminal :

```bash id="runproject"
python pfa.py
```

---

### 3. Résultat

Le programme génère automatiquement :

* Les colonnes calculées :

  * CA_Brut
  * CA_Net
  * TVA
* Le fichier :

```id="resultfile"
resultats_final.csv
```

---

## 📊 Exemple de sortie

```id="outputexample"
ID,Prix,Quantite,Remise,CA_Brut,CA_Net,TVA
101,599.99,3,10,1799.97,1619.97,323.99
```

---

## 📈 Bonus

* Visualisation graphique du CA par produit
* Lecture dynamique de fichiers CSV de tailles variables

---

## 🧠 Compétences utilisées

* Manipulation de fichiers CSV
* Structures de données en Python
* Boucles et conditions
* Calculs financiers
* Visualisation de données

---

## 👩‍💻 Auteur

* Nom : Amani Benzarti 
        Housseine Yousbachi
        Rayen Razgui
* Niveau : 2ᵉ année Mathématiques Appliquées & Data Science
* Année universitaire : 2025-2026

---

## 📄 Licence

Ce projet est réalisé dans un cadre académique.

---


---

##  Améliorations possibles

* Interface graphique (GUI)
* Analyse statistique avancée
* Intégration avec base de données
* Dashboard interactif

---
