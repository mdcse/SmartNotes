from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin #Mixin is used to redirect to login page if not logged in


class HomeView(TemplateView):
    template_name =  "home/welcome.html"
    extra_context = {'today': datetime.today()}

# def home(request):
#     return render(request, "home/welcome.html", {'today': datetime.today()})

# @login_required for login required and (login_url='login') for redirecting to login page

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, "home/authorized.html",{})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
