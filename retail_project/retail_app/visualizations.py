import matplotlib.pyplot as plt
import io
import urllib, base64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" # Fonction pour charger les données depuis le fichier Excel
def load_retail_data(file_path):
    data = pd.read_excel(file_path)
    return data"""


# Fonction pour visualiser la distribution des quantités
import pandas as pd

import io
import base64
import urllib.parse

def plot_quantity_distribution():
    # Chargement des données
    data = pd.read_excel('c:/Users/LENOVO/Desktop/Master1SBD/semestre2/python_avance/PROJET NGUEGUIM/Online Retail.xlsx')
    
    # Sélection des variables à inclure dans le graphique
    variables = ['Quantity', 'UnitPrice', 'CustomerID']
    
    # Création du graphique avec plusieurs sous-graphiques
    fig, axes = plt.subplots(nrows=len(variables), figsize=(10, 12))
    
    # Boucle sur chaque variable pour créer les sous-graphiques
    for i, var in enumerate(variables):
        sns.histplot(data[var], kde=True, bins=50, color='blue', edgecolor='k', ax=axes[i])
        axes[i].set_xlabel(var)
        axes[i].set_ylabel('Density')
        axes[i].set_title(f'Distribution of {var}')
    
    # Ajustement de l'espacement entre les sous-graphiques
    plt.tight_layout()
    
    # Sauvegarde la figure dans un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode('utf-8')
    uri = urllib.parse.quote(string)
    
    # Ferme le plot pour éviter les fuites de mémoire
    plt.close()
    
    return uri


""" # Fonction pour visualiser la relation entre le prix unitaire et la quantité
def plot_unitprice_vs_quantity(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Quantity'], data['UnitPrice'], alpha=0.5)
    plt.xlabel('Quantity')
    plt.ylabel('Unit Price')
    plt.title('Unit Price vs Quantity')

    # Sauvegarder la figure dans un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close()
    return uri

"""