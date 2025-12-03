from django import forms
from .models import Profile, Project

class ContactForm(forms.Form):
    name = forms.CharField(label="Adınız Soyadınız", widget=forms.TextInput(attrs={'placeholder': 'Örn: Ahmet Yılmaz'}))
    email = forms.EmailField(label="E-posta Adresiniz", widget=forms.EmailInput(attrs={'placeholder': 'ornek@email.com'}))
    message = forms.CharField(label='Mesajınız', widget=forms.Textarea(attrs={'placeholder': 'Mesajınızı buraya yazın...'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'subtitle', 'about_title', 'about_text']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Örn: Adınız Soyadınız'}),
            'subtitle': forms.TextInput(attrs={'placeholder': 'Örn: Web Geliştirici'}),
            'about_title': forms.TextInput(attrs={'placeholder': 'Örn: Hakkımda'}),
            'about_text': forms.Textarea(attrs={'placeholder': 'Kendinizi tanıtan kısa bir yazı girin...', 'rows': 5}),
        }
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ['title', 'description', 'image', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Proje Başlığı'}),
            'description': forms.Textarea(attrs={'placeholder': 'Proje hakkında kısa bilgi...', 'rows': 3}),
            'url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }