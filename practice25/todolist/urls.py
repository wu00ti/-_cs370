from django.conf.urls import patterns,url
from todolist import views

urlpatterns = patter('',
        url(r'^$',views.index,name='index'),
        )
