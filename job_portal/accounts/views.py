from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import EmployeeRegistrationForm, EmployeeLoginForm


def signup(request):
    next = request.GET.get('next')
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('accounts:login')

    context = {
        'form': form,
    }

    return render(request, "accounts/employee_signup.html", context)


def employee_login(request):
    next = request.GET.get('next')
    form = EmployeeLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(420)
                login(request, user)
                return redirect('/')
    context = {
        'form': form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')