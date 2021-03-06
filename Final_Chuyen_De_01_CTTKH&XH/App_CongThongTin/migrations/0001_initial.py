# Generated by Django 3.1.2 on 2020-10-16 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tblDanhMucBaiViet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenDanhMuc', models.CharField(max_length=300)),
                ('MaDanhMUc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tblImageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaHinhAnh', models.CharField(max_length=20)),
                ('Image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('Name', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='tblLinhVuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaLinhVuc', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tblLoaiVB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maloaivb', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=200)),
                ('Type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tblPhongBan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaPhongBan', models.CharField(max_length=20)),
                ('TenPhongBan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblVanBan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaVanBan', models.CharField(max_length=20)),
                ('SoHieu', models.CharField(max_length=300)),
                ('NgayBanHanh', models.DateField()),
                ('NgayHieuLuc', models.DateField()),
                ('MoTa', models.CharField(max_length=400)),
                ('HetHieuLuc', models.BooleanField()),
                ('LinhVuc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CongThongTin.tbllinhvuc')),
                ('LoaiVB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CongThongTin.tblloaivb')),
            ],
        ),
        migrations.CreateModel(
            name='tbltinBai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaTinBai', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=300)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=99999999)),
                ('Detail', models.TextField(max_length=99999999)),
                ('TrangThai', models.BooleanField()),
                ('NgayDang', models.DateField()),
                ('DanhMuc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CongThongTin.tbldanhmucbaiviet')),
                ('Images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CongThongTin.tblimagecategory')),
            ],
        ),
        migrations.CreateModel(
            name='tblTacGia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaTacGia', models.CharField(max_length=30)),
                ('TenTacGia', models.CharField(max_length=40)),
                ('SDT', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=200)),
                ('TrangThai', models.BooleanField(default=False)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('PhongBan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CongThongTin.tblphongban')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-SDT', '-Email'],
            },
        ),
    ]
