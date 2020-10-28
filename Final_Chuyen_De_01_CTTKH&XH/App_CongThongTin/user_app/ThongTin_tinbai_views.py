from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.base import TemplateView,TemplateResponseMixin,ContextMixin
from django.utils.decorators import method_decorator
from ..models import *
from django.urls import reverse_lazy
from ..forms import *


class HomeView(ListView):
	model = tbltinBai
	template_name = 'them/tinbai/home_tinbai.html'
	#queryset = tblLinhVuc.objects.all()[:5]
	context_object_name = 'tinbai'

class TinBaiDetailView(DetailView):
	model = tbltinBai
	template_name = 'them/tinbai/tinbai_detail.html'
	context_object_name = 'tinbai'

class CreateTinBaiView(CreateView):
	#model = tbltinBai
	template_name = 'them/tinbai/new_tinbai.html'
	#fields = '__all__'
	form_class = TinBai
	context_object_name = 'tinbai'

	def form_valid(self, form):
		return super(CreateTinBaiView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy("news:home-tinbai")

class TinBaiEditView(UpdateView):
	model = tbltinBai
	template_name = 'them/tinbai/edit_tinbai.html'
	fields = '__all__'
	context_object_name = 'tinbai'

class TinBaiDeleteView(DeleteView):
	model = tbltinBai
	template_name = 'them/tinbai/delete_tinbai.html'
	context_object_name = 'tinbai'
	success_url = reverse_lazy('news:home-tinbai')