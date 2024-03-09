from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm


class CustomLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
        return render(request, self.template_name, {'form': form})
