from django.urls import path
from django.conf.urls import url
from . import views
from .views import remove

urlpatterns=[
path('addtask/',views.addtask, name='addtaskview'),
path('',views.home,name='home'),
url(r'^remove/(?P<pk>\d+)$', remove,name='remove'),
]