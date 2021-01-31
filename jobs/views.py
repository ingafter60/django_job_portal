# jobs/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Job 

class HomeView(ListView):

	model 				= Job
	context_object_name = 'jobs'
	paginate_by 		= 2
	template_name 		= 'jobs/index.html'
