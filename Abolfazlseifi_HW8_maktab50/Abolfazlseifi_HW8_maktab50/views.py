from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import contactForm, loginForm, registerForm


def home_page(request):
    context = {
        'title': 'home page',
        'content': 'This is MySite',
    }

    return render(request, "index.html", context)


def contact_page(request):
    contact_form = contactForm(request.POST or None)
    context = {
        'title': 'contact page',
        'content': 'This is contact page',
        'form': contact_form,
    }

    if contact_form.is_valid():
        result = contact_form.cleaned_data
        print(result)

    return render(request, 'contact_page.html', context)


def login_page(request):
    form = loginForm(request.POST or None)
    context = {
        'title': 'login page',
        'content': 'This is login page',
        'form': form,
    }

    if form.is_valid():
        data = form.cleaned_data
        print(data)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            context['form'] = loginForm()
            return redirect("/")
        else:
            print("Error")

    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = registerForm(request.POST or None)
    context = {
        'title': 'register page',
        'content': 'This is register page',
        'form': form,
    }

    if form.is_valid():
        data = form.cleaned_data
        print(data)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        User.objects.create_user(username=username, password=password, email=email)
        return redirect("/login")

    return render(request, 'auth/register.html', context)
