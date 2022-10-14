import string
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DeleteView
from urlshorter.models import Domain,ShortLink
from urlshorter.tasks import generate_shortlink
from django.urls import reverse_lazy
import random



class CreateShortLinkView(View):
    """class creates short link object"""
    def post(self,request,*args, **kwargs):
        long_url =request.POST['url']
        protocol = get_object_or_404(Domain, id=1)
        link = generate_shortlink()
        print('result: ',link)
        short_link = ShortLink(domen=protocol,long_url=long_url,short_url=link,user=request.user)
        short_link.save()
        return redirect('shorter')



class UrlShorterPageView(TemplateView):
    """url shorter page"""
    template_name = 'urlshorter/shorter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_short_links = ShortLink.objects.filter(user=self.request.user)
        context['user_short_links']=user_short_links
        return context



class GetRedirectView(View):
    """redirect by short link"""
    def get(self,request,shortlink):
        short_link = get_object_or_404(ShortLink, short_url=shortlink)
        short_link.clicks += 1
        short_link.save()
        return redirect(short_link.long_url)



class DeleteShortLinkView(View):
    """to delete the short link"""
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        short_link = get_object_or_404(ShortLink,id=pk)
        short_link.delete()
        return redirect('shorter')




def generate_shortlink():
    """function generates string sequence"""
    link = [''.join(random.choice(string.digits + string.ascii_letters) for _ in range(7))]
    return link[0].lower()
