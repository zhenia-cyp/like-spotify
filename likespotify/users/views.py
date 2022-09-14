from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic.base import TemplateView
from users.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from users.models import Profile
from playlists.models import Album
from django.contrib.auth import logout



class LogOutView(View):
    """log out class"""
    def get(self, request):
        logout(request)
        return redirect('home')



class ProfilePageView(TemplateView):
    """this class leads to the profile page """
    template_name = 'users/profile.html'



class LoginUserView(View):
    """this class makes authentication for the new user"""
    def post(self,request):
        loginform = AuthenticationForm(request,data=request.POST)

        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    print('*',loginform.errors)
                    return redirect('authorizpage')

        else:
            print('**', loginform.errors)
            return render(request, 'users/login.html', {'loginform':loginform})



class AuthorizationPageView(TemplateView):
    """this class leads to the page with the login form"""
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loginform = AuthenticationForm(self.request)
        context['loginform'] = loginform
        return context



class RegistrationView(View):
    """new user registration"""
    def get(self, request):
        template = 'users/index.html'
        reg_form = UserForm()
        return render(request, template, {'reg_form':reg_form})

    def post(self, request):
            template = 'users/index.html'
            reg_form = UserForm(request.POST)
            if reg_form.is_valid():
                 reg_form.save()
                 return redirect('authorizpage')

            else:
                print('**', reg_form.errors)
                return render(request, template, {'reg_form': reg_form})


