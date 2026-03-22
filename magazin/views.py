from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from magazin.forms import MagazinForms, ProfilForms
from magazin.models import Magazin, Profil, Savol, Tanlash
from django.contrib.auth.decorators import permission_required


def magazin_list(request):
    list = Magazin.objects.all()
    return render(request, 'magazin/magazin_list.html', {'list': list})

@permission_required('magazin.add_magazin', login_url='/users/login/')
def magazin_create(request):
    if request.method == 'POST':
        form = MagazinForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('magazin:magazin_list')
    else:
        form = MagazinForms()
    return render(request, 'magazin/magazin_create.html', {'form':form})

@permission_required('magazin.delete_magazin')
def magazin_delete(request, id):
    magazin = get_object_or_404(Magazin, id=id)
    magazin.delete()
    return redirect("magazin:magazin_list")

@permission_required('magazin.change_magazin', login_url='/users/login/')
def magazin_update(request, id):
    magazin = get_object_or_404(Magazin, id=id)
    if request.method == 'POST':
        form = MagazinForms(request.POST, request.FILES, instance=magazin)
        if form.is_valid():
            form.save()
            return redirect('magazin:magazin_list')
    else:
        form = MagazinForms(instance=magazin)
    return render(request, 'magazin/magazin_create.html', {'form':form})


# Profil qismi

def profil_list(request):
    profil = Profil.objects.all()
    return render(request, 'magazin/profil_list.html', {'profil':profil})

@login_required(login_url='/users/login/')
def profil_create(request):
    if request.method == 'POST':
        form = ProfilForms(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.user = request.user
            profil.save()
            return redirect('magazin:profil_list')
    else:
        form = ProfilForms()
    return render(request, 'magazin/profil_create.html', {'form': form})

def profil_delete(request, id):
    profil = get_object_or_404(Profil, id=id)
    profil.delete()
    return redirect('magazin:profil_list')

def profil_update(request, id):
    profil = get_object_or_404(Profil, id=id)
    if request.method == 'POST':
        form = ProfilForms(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('magazin:profil_list')
    else:
        form = ProfilForms(instance=profil)
    return render(request, 'magazin/profil_create.html', {'form':form})






# def savol_list(request, id):
#     savol = Savol.objects.all()
#     return render(request, 'magazin/savol_list.html', {'savol':savol})
#
# def variant_tanlash(request, id):
#     savol = get_object_or_404(Savol, id=id)
#     variantlar = savol.variantla.all()
#
#     if request.method == 'POST':
#


























