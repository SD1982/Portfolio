from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home, name='home'),
    path('parcours', views.resume, name='resume'),
    path('projets', views.projects, name='realisation'),
    path('competences', views.skills, name='competence'),
]
