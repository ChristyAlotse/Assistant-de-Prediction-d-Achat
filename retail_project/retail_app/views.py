# iris_app/views.py
from django.shortcuts import render
from .forms import RetailForm
from .visualizations import plot_quantity_distribution
import joblib
import numpy as np
import pandas as pd

# Charger le modèle
model = joblib.load ('retail_app/model.joblib')
#model = joblib.load('retail_app/knn_model.joblib')


#Appel de la page d'accueil
def home(request):
    return render(request, 'home.html')


def style(request):
    return render(request, 'style.css')



# Charger le modèle entraîné
#model = joblib.load('retail_app/model.joblib')


#Fonction de prédiction
def predict_retail(request):
    if request.method == 'POST':
        form = RetailForm(request.POST)
        if form.is_valid():
            unit_price = form.cleaned_data['UnitPrice']
            input_data = np.array([[unit_price]])
            
            prediction = model.predict(input_data)[0]
            predicted_quantity = round(prediction, 2)

            return render(request, 'result.html', {'result': predicted_quantity})
    else:
        form = RetailForm()
    return render(request, 'predict.html', {'form': form})



#Fonction de visualisation
def visualize_retail(request):
    plot_uri = plot_quantity_distribution()
    return render(request, 'visualize.html', {'plot_uri': plot_uri})
