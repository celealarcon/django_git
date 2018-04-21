# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#Clase que guarda la información de la última vez que se consultó a la API
class UpdateInfo(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(blank=True, null=True)
	class Meta:
		db_table = "updateinfo"

#Clase que guarda el repositorio obtenido
class Repo(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	creation_date = models.DateTimeField(blank=True, null=True)
	last_commit_date = models.DateTimeField(blank=True, null=True)
	class Meta:
		db_table = "repo"