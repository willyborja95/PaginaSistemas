from django.conf.urls import url, include
from login import views
from rest_framework.authtoken import views as viewsToken

urlpatterns=[
    #url(r'login/', views.login, name="login" ),
    url(r'^login$', views.login),
    url(r'^get$', views.ListTodo.as_view()),
    #url(r'api-token-auth/', viewsToken.obtain_auth_token, name="api-token-auth" ),    
]