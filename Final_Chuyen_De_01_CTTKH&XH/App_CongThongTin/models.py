from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.



class tblLinhVuc(models.Model):
    MaLinhVuc = models.CharField(max_length=20,blank=False,null=False)
    Name = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('news:linhvuc-detail', args=(str(self.id)))

class tblPhongBan(models.Model):
    MaPhongBan = models.CharField(max_length=20)
    TenPhongBan = models.CharField(max_length=200)
    def __str__(self):
        return self.TenPhongBan

    def get_absolute_url(self):
        return reverse('news:phongban-detail', args=(str(self.id)))

class tblLoaiVB(models.Model):
    Maloaivb = models.CharField(max_length=30)
    Name = models.CharField(max_length=200)
    Type = models.IntegerField()

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('news:loaivanban-detail', args=(str(self.id)))

class tblImageCategory(models.Model):
    MaHinhAnh = models.CharField(max_length=20)
    Image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Name = models.CharField(max_length=300)
    Description = models.CharField(max_length=300)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('news:image-detail', args=(str(self.id)))


class tblDanhMucBaiViet(models.Model):
    TenDanhMuc = models.CharField(max_length=300)
    MaDanhMUc = models.CharField(max_length=30)

    def __str__(self):
        return self.TenDanhMuc



class tbltinBai(models.Model):
    MaTinBai = models.CharField(max_length=30)
    Name = models.CharField(max_length=300)
    Title = models.CharField(max_length=200)
    Images = models.ForeignKey(tblImageCategory,on_delete=models.CASCADE)
    DanhMuc = models.ForeignKey(tblDanhMucBaiViet,on_delete=models.CASCADE)
    Description = models.TextField(max_length=99999999)
    Detail = models.TextField(max_length=99999999)
    TrangThai= models.BooleanField()
    NgayDang = models.DateField()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('news:tinbai-detail', args=(str(self.id)))



class tblVanBan(models.Model):
    MaVanBan = models.CharField(max_length=20)
    SoHieu = models.CharField(max_length=300)
    NgayBanHanh = models.DateField()
    NgayHieuLuc = models.DateField()
    MoTa = models.CharField(max_length=400)
    LoaiVB = models.ForeignKey(tblLoaiVB,on_delete=models.CASCADE)
    HetHieuLuc = models.BooleanField()
    LinhVuc = models.ForeignKey(tblLinhVuc,on_delete=models.CASCADE)

    def __str__(self):
        return self.MaVanBan

    def get_absolute_url(self):
        return reverse('news:vanban-detail', args=(str(self.id)))

class tblTacGia(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    MaTacGia = models.CharField(max_length=30)
    TenTacGia = models.CharField(max_length=40)
    PhongBan = models.ForeignKey(tblPhongBan,on_delete=models.CASCADE)
    SDT = models.CharField(max_length=30)
    Email = models.EmailField(max_length=200)
    TrangThai = models.BooleanField(default=False)
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.TenTacGia

    def get_absolute_url(self):
        return reverse('news:tacgia-detail', args=(str(self.id)))

    class Meta:
        ordering = ["-SDT","-Email"]


