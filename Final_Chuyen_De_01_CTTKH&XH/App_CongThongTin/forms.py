from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import *
from django.contrib.auth.decorators import login_required

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ""
        self.fields['username'].placeholder = "Username"
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ""
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields[
            'password1'].help_text = '<span class="form-text text-muted"><small><ul><li>Your password cant be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password cant be a commonly used password.</li><li>Your password cant be entirely numeric.</li></ul></small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class EditPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(EditPasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = ""

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = ""
        self.fields[
            'new_password1'].help_text = '<span class="form-text text-muted"><small><ul><li>Your password cant be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password cant be a commonly used password.</li><li>Your password cant be entirely numeric.</li></ul></small></span>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ""
        self.fields[
            'new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class LinhVuc(forms.ModelForm):
    class Meta:

        model = tblLinhVuc
        fields = ('MaLinhVuc', 'Name',)

class PhongBan(forms.ModelForm):
    class Meta:
        model = tblPhongBan
        fields = ('MaPhongBan', 'TenPhongBan',)
        MaPhongBan = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
        TenPhongBan = forms.EmailField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Email'}))

class LoaiVB(forms.ModelForm):
    class Meta:
        model = tblLoaiVB
        fields = ('Maloaivb','Name', 'Type',)

class Image(forms.ModelForm):
    class Meta:
        model = tblImageCategory
        fields = ('MaHinhAnh','Image', 'Name','Description',)

class TinBai(forms.ModelForm):
    class Meta:
        model = tbltinBai
        fields = ('MaTinBai','Name','Title','DanhMuc', 'Images','Description','Detail','TrangThai','NgayDang',)

    def __init__(self, *args, **kwargs):
        super(TinBai, self).__init__(*args, **kwargs)
        self.fields['MaTinBai'].widget.attrs['class'] = 'form-control'
        self.fields['Name'].widget.attrs['class'] = 'form-control'
        self.fields['DanhMuc'].widget.attrs['class'] = 'form-control'
        self.fields['Title'].widget.attrs['class'] = 'form-control'
        self.fields['Images'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'
        self.fields['Detail'].widget.attrs['class'] = 'form-control'
        self.fields['TrangThai'].widget.attrs['class'] = 'form-control'
        self.fields['NgayDang'].widget.attrs['class'] = 'form-control'

class VanBan(forms.ModelForm):
    class Meta:
        model = tblVanBan
        fields = ('MaVanBan', 'SoHieu', 'NgayBanHanh', 'NgayHieuLuc', 'MoTa', 'LoaiVB', 'HetHieuLuc', 'LinhVuc', )

    def __init__(self, *args, **kwargs):
        super(VanBan, self).__init__(*args, **kwargs)
        self.fields['MaVanBan'].widget.attrs['class'] = 'form-control'
        self.fields['SoHieu'].widget.attrs['class'] = 'form-control'
        self.fields['NgayBanHanh'].widget.attrs['class'] = 'form-control'
        self.fields['NgayHieuLuc'].widget.attrs['class'] = 'form-control'
        self.fields['MoTa'].widget.attrs['class'] = 'form-control'
        self.fields['LoaiVB'].widget.attrs['class'] = 'form-control'
        self.fields['HetHieuLuc'].widget.attrs['class'] = 'form-control'
        self.fields['LinhVuc'].widget.attrs['class'] = 'form-control'

class TacGia(forms.ModelForm):
    class Meta:
        model = tblTacGia
        fields = ('MaTacGia', 'TenTacGia', 'PhongBan', 'SDT', 'Email',)

    def __init__(self, *args, **kwargs):
        super(TacGia, self).__init__(*args, **kwargs)
        self.fields['MaTacGia'].widget.attrs['class'] = 'form-control'
        self.fields['TenTacGia'].widget.attrs['class'] = 'form-control'
        self.fields['PhongBan'].widget.attrs['class'] = 'form-control'
        self.fields['SDT'].widget.attrs['class'] = 'form-control'
        self.fields['Email'].widget.attrs['class'] = 'form-control'




class MyForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))

