from django.shortcuts import render, redirect
from .models import Accounts
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import createAccountforms
from django.forms import BaseFormSet
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

class BaseAccountFormSet(BaseFormSet):
       def clean(self):
           if any(self.errors):
               return
           emails = []
           for form in self.forms:
               email = form.cleaned_data.get('email')
               if email in emails:
                   raise forms.ValidationError("Emails must be unique.")
               emails.append(email)

class AccountPageView(CreateView):
    model = Accounts
    form_class = createAccountforms
    template_name = 'account/account.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data['email']
        user.save()
        messages.success(self.request, 'Account created successfully! Please log in.')
        return redirect('login')

# Create your views here.
def createAccount(request):
    if request.method == 'POST':
        form = createAccountforms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    form = createAccountforms()
    return render(request, 'account/account.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movie')  # GET redirect to movie page
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})
