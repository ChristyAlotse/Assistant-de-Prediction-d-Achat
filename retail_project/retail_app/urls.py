# iris_app/urls.py
from django.urls import path
from .views import home, predict_retail, visualize_retail, style

urlpatterns = [
    path('', home, name='home'),
    path('predict/', predict_retail, name='predict_retail'),
    path('visualize/', visualize_retail, name='visualize_retail'),
    path('', style, name='style')
]
