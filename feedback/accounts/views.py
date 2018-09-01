from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    next_page = request.GET.get('next')
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_page'))

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))

            if user is not None:
                if user.is_active:
                    login(request, user)

                    success_message = "Welcome {}! You have been logged in.".format(username.title())
                    messages.success(request, success_message)

                    if next_page:
                        return HttpResponseRedirect(next_page)

                    return HttpResponseRedirect(reverse('home_page'))

                messages.error(request, "Account deactivated! Email admin for help.")

            messages.error(request, "Login failed! Username and/or password invalid")

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form, })


def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_page'))

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            user = authenticate(
                username=username,
                password=form.cleaned_data.get('password1'))

            if user and user.is_active:
                login(request, user)

                success_message = "Account created successfully! Welcome {}!".format(username.title())
                messages.success(request, success_message)

                return HttpResponseRedirect(reverse('home_page'))

            messages.error(request, "Account registered! Check email for admin message.")

        messages.error(request, "Registration failed! Check listed errors.")

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form, })


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")

    return HttpResponseRedirect(reverse('home_page'))
