from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

from curriculum.models import Competence, Diplome, Experience, Realisation


def home(request):
    return render(request, 'curriculum/accueil.html', {'date': datetime.now()})


def resume(request):
    experiences = Experience.objects.all()
    diplomes = Diplome.objects.all()
    return render(request, 'curriculum/parcours.html',
                  {'experiences': experiences,
                   'diplomes': diplomes, })


def projects(request):
    realisations = Realisation.objects.all()
    return render(request, 'curriculum/projets.html',
                  {'realisations': realisations, })


def skills(request):
    competences = Competence.objects.all()
    return render(request, 'curriculum/competences.html',
                  {'competences': competences, })
