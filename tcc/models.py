from django.db import models

class Dispositivo(models.Model):
    
    STATUS = (
        ('funciona', 'Funciona'),
        ('estragado', 'Estragado'),
    )

    nome = models.CharField(max_length=255, null=False)
    descricao = models.TextField(null=False)
    funcionamento = models.CharField(
        null=False,
        default='func',
        max_length=9,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):

    idProf = models.IntegerField
    idDisp = models.IntegerField
    diaEmprestimo = models.DateField
    horaRecolhimento = models.TimeField
    horaDevolucao = models.TimeField

class Professor(models.Model):

    nome = models.CharField(max_length=45, blank=False, null=False)
    matricula = models.CharField(max_length=15, unique=True, blank=False, null=False)
    email = models.CharField(max_length=35, default='', unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome

class Secretaria(models.Model):
    
    nome = models.CharField(max_length=45, blank=False, null=False)
    matricula = models.CharField(max_length=15, unique=True, blank=False, null=False)
    email = models.CharField(max_length=35, default='', unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome

class Usuario(models.Model):

    nome = models.CharField(max_length=45, blank=False, null=False)
    matricula = models.CharField(max_length=15, unique=True, blank=False, null=False)
    email = models.CharField(max_length=35, default='', unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome