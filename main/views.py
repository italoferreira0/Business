from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class AnaliseView(LoginRequiredMixin, TemplateView):
    template_name = 'analise.html'

class CarteiraView(LoginRequiredMixin, TemplateView):
    template_name = 'carteira.html'

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')