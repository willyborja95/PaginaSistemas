from django.conf.urls import url, include
from login import views

urlpatterns=[
    url(r'^login$', views.login, name="login" ),
]