from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic.base import TemplateView
from users.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from users.models import Profile
from playlists.models import Album


class ProfilePageView(TemplateView):
    """this class leads to the profile page """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile']= profile
        albums = Album.objects.filter(user=self.request.user)
        context['albums'] = albums
        return context




class LoginUserView(View):
    """this class makes authentication for the new user"""
    def post(self,request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # print('***',user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('authorizpage')

        else:
            return redirect('authorizpage')



class AuthorizationPageView(TemplateView):
    """this class leads to the page with the login form"""
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_form = LoginForm()
        context['loginform'] = login_form
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

