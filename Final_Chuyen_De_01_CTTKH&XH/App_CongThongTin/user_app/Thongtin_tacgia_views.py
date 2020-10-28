from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from ..forms import *


class HomeView(ListView):
	model = tblTacGia
	template_name = 'them/TacGia/tacgia-home.html'
	context_object_name = 'tacgia'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context

	def get_queryset(self):
		#queryset = super(HomeView, self).get_queryset().order_by() query database
		return super(HomeView, self).get_queryset()

class TacGiaDetailView(DetailView):
	model = tblTacGia
	template_name = 'them/TacGia/tacgia_detail.html'
	#paginate_by = 100  # phan trang

	context_object_name = 'tacgia'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#print(context)
		return context


class CreateTacGiaView(CreateView):
	#model = tblTacGia
	template_name = 'them/TacGia/new_tacgia.html'
	form_class = TacGia
	#fields = '__all__'
	#context_object_name = 'tacgia'

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.TrangThai = True
		return super(CreateTacGiaView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy("news:home")


class TacGiaEditView(UpdateView):
	model = tblTacGia
	template_name = 'them/TacGia/edit_tacgia.html'
	fields = ['TenTacGia','PhongBan','SDT']
	context_object_name = 'tacgia'


class TacGiaDeleteView(DeleteView):
	model = tblTacGia
	template_name = 'them/TacGia/delete_tacgia.html'
	context_object_name = 'tacgia'
	success_url = reverse_lazy('news:home')
