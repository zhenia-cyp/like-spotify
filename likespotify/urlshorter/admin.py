from django.contrib import admin
from django.contrib import admin
from urlshorter.models import Domain,ShortLink



class DomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Domain,DomainAdmin)

class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url',)

admin.site.register(ShortLink,ShortLinkAdmin)

