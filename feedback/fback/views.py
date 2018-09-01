from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

User = get_user_model()


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'fback/form.html'

    def get_success_url(self):
        messages.success(self.request, 'Thank you for your feedback!')
        return reverse('accounts:logout')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = User.objects.get(username=self.request.user)
        f.save()
        return HttpResponseRedirect(self.get_success_url())


def success(request):
    return render(request, 'fback/success.html')
