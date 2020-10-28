from logging import PlaceHolder

from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy

class HomeView(ListView):
	model = tblPhongBan
	template_name = 'them/PhongBan/home_phongban.html'
	#queryset = tblPhongBan.objects.all()[:5]
	context_object_name = 'phongban'



class PhongBanDetailView(DetailView):
	model = tblPhongBan
	template_name = 'them/PhongBan/phongban_detail.html'
	context_object_name = 'phongban'



class CreatePhongBanView(CreateView):
	model = tblPhongBan
	template_name = 'them/PhongBan/new_phongban.html'
	fields = '__all__'


class PhongBanEditView(UpdateView):
	model = tblPhongBan
	template_name = 'them/PhongBan/edit_phongban.html'
	fields = '__all__'
	context_object_name = 'phongban'
	success_url = reverse_lazy('news:home-phongban')


class PhongBanDeleteView(DeleteView):
	model = tblPhongBan
	template_name = 'them/PhongBan/delete_phongban.html'
	context_object_name = 'phongban'
	success_url = reverse_lazy('news:home-phongban')
