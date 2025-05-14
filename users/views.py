from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.utils.http import url_has_allowed_host_and_scheme ## prevents open redirects
from django.conf import settings

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
        return redirect('home:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})



def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
	            return redirect(next_url)
            return redirect('home:index')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'next': next_url})



def logout_view(request):
    logout(request)
    return redirect('users:login')