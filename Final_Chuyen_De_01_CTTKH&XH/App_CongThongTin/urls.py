from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .user_app import Thongtin_tacgia_views,\
    ThongTin_phongban_views,\
    user_views,\
    ThongTin_linhvuc_views,\
    ThongTin_loaivanban_views,\
    ThongTin_image_views,\
    ThongTin_tinbai_views,\
    ThongTin_vanban_views,\
    ThongTin_Nguoidung_views


app_name = 'news'
urlpatterns = [

    path('lienhe/', ThongTin_Nguoidung_views.lienhe, name='lienhe'),
    path('gioithieu1/', ThongTin_Nguoidung_views.gioithieu1, name='gioithieu1'),
    path('gioithieu2/', ThongTin_Nguoidung_views.gioithieu2, name='gioithieu2'),
    path('gioithieu3/', ThongTin_Nguoidung_views.gioithieu3, name='gioithieu3'),
    path('gioithieu4/', ThongTin_Nguoidung_views.gioithieu4, name='gioithieu4'),
    path('ykien/', ThongTin_Nguoidung_views.ykien, name='ykien'),
    path('', ThongTin_Nguoidung_views.viewlist, name='danhmuc'),
    path('danhmuc/<int:pk>', ThongTin_Nguoidung_views.detailviews, name="danhmuc-detail"),
    path('danhmuc/baiviet/<int:baiviet_id>', ThongTin_Nguoidung_views.detailview_baiviet, name="baiviet-detail"),

    #user login logout edit
    path('login/', user_views.login_user, name='login'),
    path('logout/', user_views.logout_user, name='logout'),
    path('register/', user_views.register_user, name='register'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path('change_password/', user_views.change_password, name='change_password'),

#tac gia
    path('admin_page/login/', Thongtin_tacgia_views.HomeView.as_view(), name ='home'),
    path('tacgia/new/', Thongtin_tacgia_views.CreateTacGiaView.as_view(), name="tacgia-new"),
    path('tacgia/<int:pk>', Thongtin_tacgia_views.TacGiaDetailView.as_view(), name="tacgia-detail"),
    path('tacgia/<int:pk>/edit/', Thongtin_tacgia_views.TacGiaEditView.as_view(), name="tacgia-edit"),
    path('tacgia/<int:pk>/remove/', Thongtin_tacgia_views.TacGiaDeleteView.as_view(), name='tacgia-delete'),

# Linh vuc
    path('home_linhvuc', ThongTin_linhvuc_views.HomeView.as_view(), name='home-linhvuc'),
    path('linhvuc/new/', ThongTin_linhvuc_views.CreateLinhVucView.as_view(), name="linhvuc-new"),
    path('linhvuc/<int:pk>/', ThongTin_linhvuc_views.LinhvucDetailView.as_view(), name="linhvuc-detail"),
    path('linhvuc/<int:pk>/edit/', ThongTin_linhvuc_views.LinhvucEditView.as_view(), name="linhvuc-edit"),
    path('linhvuc/<int:pk>/remove/', ThongTin_linhvuc_views.LinhvucDeleteView.as_view(), name='linhvuc-delete'),

# Phong ban
    path('home_phongban', ThongTin_phongban_views.HomeView.as_view(), name='home-phongban'),
    path('phongban/new/', ThongTin_phongban_views.CreatePhongBanView.as_view(), name="phongban-new"),
    path('phongban/<int:pk>/', ThongTin_phongban_views.PhongBanDetailView.as_view(), name="phongban-detail"),
    path('phongban/<int:pk>/edit/', ThongTin_phongban_views.PhongBanEditView.as_view(), name="phongban-edit"),
    path('phongban/<int:pk>/remove/', ThongTin_phongban_views.PhongBanDeleteView.as_view(), name='phongban-delete'),

# Phong loai van ban
    path('home_loaivanban', ThongTin_loaivanban_views.HomeView.as_view(), name='home-loaivanban'),
    path('loaivanban/new/', ThongTin_loaivanban_views.CreateLoaiVanBanView.as_view(), name="loaivanban-new"),
    path('loaivanban/<int:pk>/', ThongTin_loaivanban_views.LoaiVanBanDetailView.as_view(), name="loaivanban-detail"),
    path('loaivanban/<int:pk>/edit/', ThongTin_loaivanban_views.LoaiVanBanEditView.as_view(), name="loaivanban-edit"),
    path('loaivanban/<int:pk>/remove/', ThongTin_loaivanban_views.LoaiVanBanDeleteView.as_view(), name='loaivanban-delete'),

# Image
    path('home_image', ThongTin_image_views.HomeView.as_view(), name='home-image'),
    path('image/new/', ThongTin_image_views.CreateImageView.as_view(), name="image-new"),
    path('image/<int:pk>/', ThongTin_image_views.ImageDetailView.as_view(), name="image-detail"),
    path('image/<int:pk>/edit/', ThongTin_image_views.ImageEditView.as_view(), name="image-edit"),
    path('image/<int:pk>/remove/', ThongTin_image_views.ImageDeleteView.as_view(), name='image-delete'),

# Tin Bai
    path('home_tinbai', ThongTin_tinbai_views.HomeView.as_view(), name='home-tinbai'),
    path('tinbai/new/', ThongTin_tinbai_views.CreateTinBaiView.as_view(), name="tinbai-new"),
    path('tinbai/<int:pk>/', ThongTin_tinbai_views.TinBaiDetailView.as_view(), name="tinbai-detail"),
    path('tinbai/<int:pk>/edit/', ThongTin_tinbai_views.TinBaiEditView.as_view(), name="tinbai-edit"),
    path('tinbai/<int:pk>/remove/', ThongTin_tinbai_views.TinBaiDeleteView.as_view(), name='tinbai-delete'),


# vanban
    path('home_vanban', ThongTin_vanban_views.HomeView.as_view(), name='home-vanban'),
    path('vanban/new/', ThongTin_vanban_views.CreateVanBanView.as_view(), name="vanban-new"),
    path('vanban/<int:pk>/', ThongTin_vanban_views.VanBanDetailView.as_view(), name="vanban-detail"),
    path('vanban/<int:pk>/edit/', ThongTin_vanban_views.VanBanEditView.as_view(), name="vanban-edit"),
    path('vanban/<int:pk>/remove/', ThongTin_vanban_views.VanBanDeleteView.as_view(), name='vanban-delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)