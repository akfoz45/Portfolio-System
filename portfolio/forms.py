from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Adınızı Soyadınız", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Ahmet Yılmaz'}))
    email = forms.EmailField(label="E-posta Adresiniz", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ornek@email.com'}))
    message = forms.CharField(label='Mesajınız', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Mesajınızı buraya yazın...'}))