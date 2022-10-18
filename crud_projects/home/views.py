from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations

class HomeView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'home/main.html', context)

def logout_view(request):
  logout(request)
  return redirect("/")

class SignUp(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('home:login')
   template_name = 'registration/signup.html'