from django.urls import path
from . import views

app_name="app2"

urlpatterns = [
    path('ofertas/', views.ofertas, name='ofertas'),
    path('contacto/', views.contacto, name='contacto'),
]