from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserRegisterForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('magazin:magazin_list')
#     else:
#         form = UserRegisterForm()
#     group = Group.objects.get(name='user')
#     user.groups.add(group)
#     return render(request, 'users/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='User')
            user.groups.add(group)

            login(request, user)
            return redirect('magazin:magazin_list')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('magazin:magazin_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('magazin:magazin_list')
