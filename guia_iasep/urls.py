from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from guia import views as guia_views

urlpatterns = [
    # administrative routes 
    path('.admin', admin.site.urls),
    url(r'^\.well-known/', include('letsencrypt.urls')),
    
    # medical guide routes
    path('', guia_views.homepage, name="homepage"),
    path('<slug:city_slug>', guia_views.city_detail, name="city_detail"),
    path('<slug:city_slug>/<slug:service_slug>',guia_views.places_listing, name='places_listing'),
]

