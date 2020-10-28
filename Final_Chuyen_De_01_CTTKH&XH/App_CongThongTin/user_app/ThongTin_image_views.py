from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy
from ..forms import *

class HomeView(ListView):
	model = tblImageCategory
	template_name = 'them/image/home_image.html'
	#queryset = tblLinhVuc.objects.all()[:5]
	context_object_name = 'image'

class ImageDetailView(DetailView):
	model = tblImageCategory
	template_name = 'them/image/image_detail.html'
	context_object_name = 'image'

class CreateImageView(CreateView):
	model = tblImageCategory
	template_name = 'them/image/new_image.html'
	fields = '__all__'
	context_object_name = 'image'



class ImageEditView(UpdateView):
	model = tblImageCategory
	template_name = 'them/image/edit_image.html'
	fields = '__all__'
	context_object_name = 'image'


class ImageDeleteView(DeleteView):
	model = tblImageCategory
	template_name = 'them/image/delete_image.html'
	context_object_name = 'image'
	success_url = reverse_lazy('news:home-image')
