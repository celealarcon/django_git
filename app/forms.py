# -*- coding: utf-8 -*-
from django import forms

#Formulario para filtrar repositorios mediante el nombre, usado en repo_view en views.py
class RepoForm(forms.Form):
	repo_name = forms.CharField(label='', 
								widget=forms.TextInput( 
									attrs={'placeholder': 'Buscar'}),
								max_length=200, required=False)