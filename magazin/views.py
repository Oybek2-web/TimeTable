from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from magazin.forms import TimeTableForms, ProfilForms
from magazin.models import TimeTable, Profil
from django.contrib.auth.decorators import permission_required

import qrcode
from django.http import HttpResponse
from io import BytesIO

def time_table_list(request):
    list = TimeTable.objects.all()
    return render(request, 'magazin/time_table_list.html', {'list': list})


@permission_required('magazin.add_magazin', login_url='/users/login/')
def time_table_create(request):
    if request.method == 'POST':
        form = TimeTableForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('magazin:time_table_list')
    else:
        form = TimeTableForms()
    return render(request, 'magazin/time_table_create.html', {'form':form})


@permission_required('magazin.delete_magazin')
def time_table_delete(request, id):
    magazin = get_object_or_404(TimeTable, id=id)
    magazin.delete()
    return redirect("magazin:time_table_list")


@permission_required('magazin.change_magazin', login_url='/users/login/')
def time_table_update(request, id):
    magazin = get_object_or_404(TimeTable, id=id)
    if request.method == 'POST':
        form = TimeTableForms(request.POST, request.FILES, instance=magazin)
        if form.is_valid():
            form.save()
            return redirect('magazin:time_table_list')
    else:
        form = TimeTableForms(instance=magazin)
    return render(request, 'magazin/time_table_create.html', {'form':form})



@login_required(login_url='/users/login/')
def profil_list(request):
    profil = Profil.objects.filter(user=request.user)

    context = {
        'profil': profil,
        'has_profil': profil.exists()  # 🔥 eng muhim qator
    }

    return render(request, 'magazin/profil_list.html', context)


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

@login_required(login_url='/users/login/')
def profil_delete(request, id):
    profil = get_object_or_404(Profil, id=id, user=request.user)
    profil.delete()
    return redirect('magazin:profil_list')

@login_required(login_url='/users/login/')
def profil_update(request, id):
    profil = get_object_or_404(Profil, id=id, user=request.user)

    if request.method == 'POST':
        form = ProfilForms(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('magazin:profil_list')
    else:
        form = ProfilForms(instance=profil)

    return render(request, 'magazin/profil_create.html', {'form': form})


# def qr_view(request):
#     url = "http://127.0.0.1:8000/schedule/"
#
#     qr = qrcode.make(url)
#
#     buffer = BytesIO()
#     qr.save(buffer, format="PNG")
#
#     return HttpResponse(buffer.getvalue(), content_type="image/png")

# def qr_view(request):
#     url = request.build_absolute_uri('/schedule/')
#
#     qr = qrcode.make(url)
#
#     buffer = BytesIO()
#     qr.save(buffer, format="PNG")
#
#     return HttpResponse(buffer.getvalue(), content_type="image/png")

def qr_view(request):
    url = "http://127.0.0.1:8000/magazin/list/"
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")



























