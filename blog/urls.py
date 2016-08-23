from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/$',views.list, name='list'),
    url(r'^save/$',views.save, name='save'),
    url(r'^post_list/$',views.post_list, name='post_list'),

]