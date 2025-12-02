from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Profile
from .forms import ContactForm, ProfileForm, ProjectForm
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"\n--- YENİ MESAJ GELDİ ---\nKimden: {name} ({email})\nMesaj: {message}\n------------------------\n")

            return render(request, 'portfolio/home.html', {
                'projects': projects,
                'profile': profile,
                'form': ContactForm(), 
                'success': True 
            })
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'profile':profile,
        'form': form
    })


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/detail.html', {'project': project})

@login_required(login_url='/admin/')
def edit_profile(request):
    profile, created =  Profile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'portfolio/form_edit.html', {'form': form, 'title': 'Profili Düzenle'})


@login_required(login_url='/admin/')
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/form_edit.html', {'form': form, 'title': 'Projeyi Düzenle'})

@login_required(login_url='/admin/')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/form_edit.html', {'form': form, 'title': 'Yeni Proje Ekle'})

@login_required(login_url='/admin/')
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request, 'portfolio/confirm_delete.html', {'project': project})