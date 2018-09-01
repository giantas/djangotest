from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated():
        return redirect('feedback:form')
    return render(request, 'index.html')
