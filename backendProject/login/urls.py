from django.conf.urls import url, include
from login import views
from rest_framework.authtoken import views as viewsToken
#from rest_framework.urlpatterns import format_sufifix_patterns

urlpatterns=[
    #url(r'login/', views.login, name="login" ),
    url(r'^login$', views.login),
    url(r'^usuario$', views.usuario),
    #url(r'api-token-auth/', viewsToken.obtain_auth_token, name="api-token-auth" ),    
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^category/$',views.CategoryList.as_view()),
    url(r'^itemcategory/(?P<pk>[0-9]+)/$', views.ItemCategoryDetail.as_view()),
    url(r'^itemcategory/$',views.ItemCategoryList.as_view()),
]