from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Proje Başlığı")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='portfolio/images/', verbose_name="Proje Görseli", blank=True)
    url = models.URLField(blank=True, verbose_name="Proje Linki")

    def __str__(self):
        return self.title

class Profile(models.Model):
    full_name = models.CharField(max_length=100, default="", verbose_name="Ad Soyad")
    subtitle = models.CharField(max_length=200, default="", verbose_name="Alt Başlık (Ünvan)")
    avatar = models.ImageField(upload_to='portfolio/avatar/', blank=True, null=True, verbose_name="Profil Fotoğrafı")
    about_title = models.CharField(max_length=100, default="", verbose_name="Hakkımda Başlığı")
    about_text = models.TextField(default="", verbose_name="Hakkımda Yazısı")

    def __str__(self):
        return "Kişisel Bilgiler (Profile)"
    
    class Meta:
        verbose_name = "Kişisel Bilgiler"
        verbose_name_plural = "Kişisel Bilgiler"