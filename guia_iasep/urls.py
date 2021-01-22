from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guia.urls', namespace='guia')),
    url(r'^\.well-known/', include('letsencrypt.urls'))

]
