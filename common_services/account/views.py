from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, \
    login, logout
from .forms import LoginForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('services:home')

    alert = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd.get('username'),
                                password=cd.get('password'))
            if user is not None:
                login(request, user)
                return redirect('services:home')
            alert = 'Неправильный логин или пароль!'
        else:
            alert = 'Заполните все необходимые поля!'

    form = LoginForm()
    return render(request, 'account/login.html',
                  context={'form': form,
                           'alert': alert})


def user_logout(request):
    logout(request)
    return redirect('account:login')


def page_not_found(request, exception):
    return render(request,
                  'account/404.html')
