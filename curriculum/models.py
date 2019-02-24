from datetime import datetime

from django.db import models


class Experience(models.Model):
    fonction = models.CharField(null=False, max_length=255)
    employeur = models.CharField(null=False, max_length=255)
    ville = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    debut = models.DateField(null=False, verbose_name="date de début")
    fin = models.DateField(null=False, verbose_name="date de fin")
    ajout = models.DateTimeField(default=datetime.now,
                                 verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "expérience"
        ordering = ['debut']

    def __str__(self):
        return self.fonction


class Diplome(models.Model):
    intitule = models.CharField(null=False, max_length=255)
    ecole = models.CharField(null=False, max_length=255)
    ville = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    obtenu = models.CharField(null=True, max_length=255)
    debut = models.DateField(null=False, verbose_name="date de début")
    fin = models.DateField(null=False, verbose_name="date de fin")
    ajout = models.DateTimeField(default=datetime.now,
                                 verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "diplôme"
        ordering = ['debut']

    def __str__(self):
        return self.intitule


class Competence(models.Model):
    techno = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    image = models.CharField(null=False, max_length=255)
    niveau = models.IntegerField(null=False, default=0)
    ajout = models.DateTimeField(default=datetime.now,
                                 verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "compétence"
        ordering = ['techno']

    def __str__(self):
        return self.techno


class Realisation(models.Model):
    titre = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    image = models.CharField(null=False, max_length=255)
    lien = models.URLField(null=False, max_length=255)
    code = models.URLField(null=True, max_length=255)
    ajout = models.DateTimeField(default=datetime.now,
                                 verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "réalisation"
        ordering = ['ajout']

    def __str__(self):
        return self.titre


class Info(models.Model):
    nom = models.CharField(null=False, max_length=255)
    prenom = models.CharField(null=False, max_length=255)
    photo = models.CharField(null=False, max_length=255)
    adresse = models.CharField(null=False, max_length=255)
    age = models.DateField(null=False, verbose_name="Date de naissance")
    mail = models.EmailField(null=False)
    ajout = models.DateTimeField(default=datetime.now,
                                 verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "info"

    def __str__(self):
        return self.nom
