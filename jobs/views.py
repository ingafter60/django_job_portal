# jobs/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomeView(ListView):

	template_name 		= 'jobs/index.html'
	context_object_name = 'jobs'