from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy
from ..forms import *

class HomeView(ListView):
	model = tblVanBan
	template_name = 'them/vanban/home_vanban.html'
	#queryset = tblLinhVuc.objects.all()[:5]
	context_object_name = 'vanban'

class VanBanDetailView(DetailView):
	model = tblVanBan
	template_name = 'them/vanban/vanban_detail.html'
	context_object_name = 'vanban'

class CreateVanBanView(CreateView):
	#model = tblVanBan
	template_name = 'them/vanban/new_vanban.html'
	#fields = '__all__'
	form_class = VanBan
	context_object_name = 'vanban'

	def form_valid(self, form):
		return super(CreateVanBanView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy("news:home")

class VanBanEditView(UpdateView):
	model = tblVanBan
	template_name = 'them/vanban/edit_vanban.html'
	fields = '__all__'
	context_object_name = 'vanban'

class VanBanDeleteView(DeleteView):
	model = tblVanBan
	template_name = 'them/vanban/delete_vanban.html'
	context_object_name = 'vanban'
	success_url = reverse_lazy('news:home-vanban')
