from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.views.generic import ListView,DetailView
from ..forms import *



def lienhe(request):
	return render(request,"Menu_trang/inclus/header_lienhe.html")

def gioithieu1(request):
	return render(request, "gioi-thieu/gioi-thieu-cong-thong-tin-khvacn-1.html")

def gioithieu2(request):
	return render(request, "gioi-thieu/quy-che-van-hanh-cong-thong-tin-khvacn-2.html")

def gioithieu3(request):
	return render(request, "gioi-thieu/danh-sach-ban-bien-tap-3.html")

def gioithieu4(request):
	return render(request, "gioi-thieu/co-cau-to-chuc-ban-bien-tap-5.html")

def ykien(request):
	form = MyForm()
	return render(request, "111/dong-gop-y-kien.html", {'form':form})

def viewlist(request):
	# context = {}
	# query = ""
	# if request.GET:
	# 	query = request.GET['q']
	# 	context['query'] = str(query)
	# blog_posts = sorted(get_blog_queryset(query), reverse=True)


	baiviet = tblDanhMucBaiViet.objects.all()
	vanban = tblVanBan.objects.all()
	baiviet1 = tbltinBai.objects.all().filter(DanhMuc__TenDanhMuc="Tin KH&CN Bình Dương")[:5]
	baiviet2 = tbltinBai.objects.all().filter(DanhMuc__TenDanhMuc="Kết quả nghiên cứu trong và ngoài nước")[:5]
	baiviet3 = tbltinBai.objects.all().filter(DanhMuc__TenDanhMuc="Tin KH&CN trong nước")[:5]
	baiviet4 = tbltinBai.objects.all().filter(DanhMuc__TenDanhMuc="Tin KH&CN Thế giới")[:5]
	context = {"baiviet":baiviet,
			   "vanban":vanban,
			   "baiviet1":baiviet1,
			   "baiviet2":baiviet2,
			   "baiviet3":baiviet3,
			   "baiviet4":baiviet4}
			   # "blog_posts":blog_posts}`

	return render(request,"Menu_trang/danhmucbaiviet/home_danhmuc.html",context)

def detailviews(request,pk):
	q = tblDanhMucBaiViet.objects.get(pk=pk)
	return render(request,"Menu_trang/danhmucbaiviet/danhmuc_detail.html",{"qs":q})

def detailview_baiviet(request,baiviet_id):
	q = tbltinBai.objects.get(pk=baiviet_id)
	baiviet = tbltinBai.objects.all()
	return render(request,"Menu_trang/danhmucbaiviet/baivet_detail.html",{"qs":q,"baiviet":baiviet })


def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = tbltinBai.objects.filter(
			MaTinBai__icontains=q
			).distinct()
		for post in posts:
			queryset.append(post)
	# create unique set and then convert to list
	return list(set(queryset))



