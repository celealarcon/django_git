# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from datetime import datetime 
from app.models import Repo, UpdateInfo

class RepoTest(TestCase):
	def setUp(self):
		Repo.objects.create(name="prueba",
			creation_date=datetime.now(), 
			last_commit_date=datetime.now())
class UpdateTest(TestCase):
	def setUp(self):
		UpdateInfo.objects.create(date=datetime.now())