from django import forms
from .models import Profile, Project

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Adınızı Soyadınız", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Ahmet Yılmaz'}))
    email = forms.EmailField(label="E-posta Adresiniz", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ornek@email.com'}))
    message = forms.CharField(label='Mesajınız', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Mesajınızı buraya yazın...'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'subtitle', 'avatar', 'about_title', 'about_text']
        widgets= {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}), 
            'subtitle':forms.TextInput(attrs={'class': 'form-control'}), 
            'about_title':forms.TextInput(attrs={'class': 'form-control'}), 
            'about_text':forms.Textarea(attrs={'class': 'form-control', 'rows': 5}) 
        } 
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ['title', 'description', 'image', 'url']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}), 
            'description':forms.Textarea(attrs={'class': 'form-control', 'rows':3}), 
            'url':forms.URLInput(attrs={'class': 'form-control'}) 
        }