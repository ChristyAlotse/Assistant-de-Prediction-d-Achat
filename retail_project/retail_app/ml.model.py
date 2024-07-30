import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, silhouette_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



#chargement et nettoyage des données
data=pd.read_excel('c:/Users/LENOVO/Desktop/Master1SBD/semestre2/python_avance/PROJET NGUEGUIM/Online Retail.xlsx')
data_cleaned = data.dropna()

# Préparation des données pour la régression linéaire (ex: prédiction de Quantity en fonction de UnitPrice)
X = data_cleaned[['UnitPrice']]
y = data_cleaned['Quantity']

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle de régression linéaire
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Sauvegarder le modèle entraîné
joblib.dump(reg_model, 'retail_app/model.joblib')
