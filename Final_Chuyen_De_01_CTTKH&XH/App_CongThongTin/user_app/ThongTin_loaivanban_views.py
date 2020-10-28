from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy
from ..forms import *

class HomeView(ListView):
	model = tblLoaiVB
	template_name = 'them/loaivanban/home_loaivanban.html'
	#queryset = tblLinhVuc.objects.all()[:5]
	context_object_name = 'loaivanban'

class LoaiVanBanDetailView(DetailView):
	model = tblLoaiVB
	template_name = 'them/loaivanban/loaivanban_detail.html'
	context_object_name = 'loaivanban'

class CreateLoaiVanBanView(CreateView):
	model = tblLoaiVB
	template_name = 'them/loaivanban/new_loaivanban.html'
	fields = '__all__'
	context_object_name = 'loaivanban'


class LoaiVanBanEditView(UpdateView):
	model = tblLoaiVB
	template_name = 'them/loaivanban/edit_loaivanban.html'
	fields = '__all__'
	context_object_name = 'loaivanban'


class LoaiVanBanDeleteView(DeleteView):
	model = tblLoaiVB
	template_name = 'them/loaivanban/delete_loaivanban.html'
	context_object_name = 'loaivanban'
	success_url = reverse_lazy('news:home-loaivanban')
