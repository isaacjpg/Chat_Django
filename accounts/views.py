import logging
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm

logger = logging.getLogger('accounts')

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        logger.info('User %s REGISTERED with EMAIL %s', form.cleaned_data['username'], form.cleaned_data['email'])
        return super().form_valid(form)
    
    def form_invalid(self, form):
        logger.error('User %s FAILED TO REGISTER with EMAIL %s', form.cleaned_data['username'], form.cleaned_data['email'] if form.cleaned_data.get('email') else 'NO EMAIL')
        return super().form_invalid(form)
    

