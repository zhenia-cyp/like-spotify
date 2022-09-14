
from django.urls import path
from urlshorter.views import UrlShorterPageView,CreateShortLinkView,DeleteShortLinkView

urlpatterns = [
    path("url/page/", UrlShorterPageView.as_view(), name='shorter'),
    path("create/link/", CreateShortLinkView.as_view(), ),
    path("delete/short/link/<int:pk>/", DeleteShortLinkView.as_view(), ),
]
