from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"\n--- YENİ MESAJ GELDİ ---\nKimden: {name} ({email})\nMesaj: {message}\n------------------------\n")

            return render(request, 'portfolio/contact.html', {
                'projects': projects,
                'form': ContactForm(),
                'success':True
                })
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'form': form
    })


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/detail.html', {'project': project})