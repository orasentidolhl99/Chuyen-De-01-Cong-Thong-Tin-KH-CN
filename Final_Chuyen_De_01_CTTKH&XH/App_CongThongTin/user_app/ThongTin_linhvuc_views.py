from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy
from ..forms import *

class HomeView(ListView):
	model = tblLinhVuc
	template_name = 'them/Linhvuc/home_linhvuc.html'
	#queryset = tblLinhVuc.objects.all()[:5]
	context_object_name = 'linhvuc'

class LinhvucDetailView(DetailView):
	model = tblLinhVuc
	template_name = 'them/Linhvuc/linhvuc_detail.html'
	context_object_name = 'linhvuc'

class CreateLinhVucView(CreateView):
	model = tblLinhVuc
	template_name = 'them/Linhvuc/new_linhvuc.html'
	fields = '__all__'


class LinhvucEditView(UpdateView):
	model = tblLinhVuc
	template_name = 'them/Linhvuc/edit_linhvuc.html'
	fields = '__all__'
	context_object_name = 'linhvuc'


class LinhvucDeleteView(DeleteView):
	model = tblLinhVuc
	template_name = 'them/Linhvuc/delete_linhvuc.html'
	context_object_name = 'linhvuc'
	success_url = reverse_lazy('news:home-linhvuc')
