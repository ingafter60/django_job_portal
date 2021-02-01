# jobs/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Job, Category 

class HomeView(ListView):

	model 				= Job
	context_object_name = 'jobs'
	paginate_by 		= 5
	template_name 		= 'jobs/index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context

