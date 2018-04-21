# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from github	import Github
from app.forms import RepoForm
from app.models import Repo, UpdateInfo
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime 

#Éste método consulta la API pygithub.
#Guarda los primeros diez, y los guarda en respectivos objetos de la clase Repo.
#Cabe rescatar que solo se guardan diez, si existen en la BD, solo se modifican sus atributos; en caso de no existir, se crean.
#Se guarda la fecha en la clase UpdateInfo, solo se guarda la última fecha. Esto es por las caracteristicas entendidas del proyecto.
def update(request):
	git = Github()
	user = git.get_user("githubtraining")
	if user.get_repos() is None:
		return HttpResponse('Error', content_type='json')
	i=0
	for _repo in user.get_repos():
		if i >= 10:
			break
		if Repo.objects.filter(id=i).exists():
			repo = Repo.objects.get(id=i)
		else:
			repo = Repo.objects.create(id=i)
		repo.name = _repo.name
		repo.creation_date = _repo.created_at
		repo.last_commit_date = _repo.updated_at
		repo.save()
		i += 1
	if UpdateInfo.objects.filter(id=0).exists():
		log = UpdateInfo.objects.get(id=0)
	else:
		log = UpdateInfo.objects.create(id=0)
	log.date = datetime.now()
	log.save()
	return HttpResponseRedirect('/')


#Éste es el método principal, que renderiza la vista.
#Se crea una variable global que guardará los repositorios a mostrar, enviados al template.
#Mediante una variable POST se puede modificar el orden de los repositorios.
#Se agrega un formulario que filtra repositorios por nombre.
#Además se envía al template lá última vez que se consultó a la API.
repos = Repo.objects.all()
def repo_view(request):
	global repos
	if UpdateInfo.objects.filter(id=0).exists:
		last_update = UpdateInfo.objects.get(id=0)
		print(last_update.date)
	else:
		last_update = ""
	if request.method == 'POST':
		print(request.POST.get('order'))
		form = RepoForm(request.POST)
		if request.POST.get('order') == "creation":
			return render(request, 'index.html', {'form':form, 'repos':repos.order_by("creation_date"), 'last_update':last_update})
		elif request.POST.get('order') == "commit":
			return render(request, 'index.html', {'form':form, 'repos':repos.order_by("last_commit_date"), 'last_update':last_update})
		elif request.POST.get('order') == "none":
			repos = Repo.objects.all()
			return render(request, 'index.html', {'form':form, 'repos':repos, 'last_update':last_update})
		elif form.is_valid():
			repo_name = form.cleaned_data.get('repo_name')
			repos = Repo.objects.filter(name__contains=repo_name)
			return render(request, 'index.html', {'form':form, 'repos':repos, 'last_update':last_update})
	else:
		form = RepoForm()
		repos = Repo.objects.all()
	return render(request, 'index.html', {'form':form, 'repos':repos, 'last_update':last_update})
