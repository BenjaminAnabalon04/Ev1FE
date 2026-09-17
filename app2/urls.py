from django.urls import path
from . import views

app_name="app1"

urlpatterns = [
    path('ofertas/', views.ofertas, name='ofertas'),
    path('contacto/', views.contacto, name='contacto'),
]