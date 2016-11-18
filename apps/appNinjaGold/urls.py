from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^process_gold$', views.process_gold),
    url(r'^reset$', views.reset)
]
