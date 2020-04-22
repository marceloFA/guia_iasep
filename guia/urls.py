from django.urls import path
from guia import views

app_name = 'guia'
urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('<slug:city_slug>', views.city_detail, name="city_detail"),
    path('<slug:city_slug>/<slug:service_slug>',views.places_listing, name='places_listing')
]