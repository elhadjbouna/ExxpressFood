from menuApp import views
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^products$',views.PlatApi),
    url(r'^products/([0-9]+)$',views.PlatApi),

    url(r'^carte$',views.CarteDuJourApi),
    url(r'^carte/([0-9]+)$',views.CarteDuJourApi),

       url(r'^desert$',views.DesertApi),
    url(r'^desert/([0-9]+)$',views.DesertApi),

       url(r'^livreur$',views.livreurApi),
    url(r'^livreur/([0-9]+)$',views.livreurApi),

       url(r'^Commande$',views.CommandeApi),
    url(r'^Commande/([0-9]+)$',views.CommandeApi),

       url(r'^Personne$',views.PersonneApi),
    url(r'^Personne/([0-9]+)$',views.PersonneApi),


       url(r'^Client$',views.ClientApi),
    url(r'^Client/([0-9]+)$',views.ClientApi),

    url(r'^carte/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)