from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls import url


#Navn og plassering på de ulike sidene i sidebar.

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('login/', views.login, name='registration-login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/', views.user, name='page-user'),
    path('admin/', views.admin, name='admin'),
    #path('log/', views.log, name='page-log'),
    path('addActivity/', views.addActivity, name= 'page-addActivity'),
    path('userOrOrg/', views.userOrOrg, name='userOrOrg'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.activity_delete, name='activity_delete'),
    path('reg/<int:id>/', views.registration_add, name='registration_add'),
    path('reg2/<int:id>/', views.registration_and_removefav, name='registration_and_removefav'),
    path('statistics/', views.statistics, name='page-statistics'),
]