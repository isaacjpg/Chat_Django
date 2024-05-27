import logging
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm




class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
