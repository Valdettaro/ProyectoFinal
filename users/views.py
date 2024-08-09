from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ProfileForm, UserEditForm, Profile

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña inválidos')
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserEditForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserEditForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {
        'profile_form': profile_form,
        'user_form': user_form
    })
