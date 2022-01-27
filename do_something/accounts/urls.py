from django.urls import path
from . import views
from .views import SignUpViewPriv, SignUpViewOrg



urlpatterns = [
    path('signupPriv/', SignUpViewPriv.as_view(), name='signupPriv'),
    path('signupOrg/', SignUpViewOrg.as_view(), name='signupOrg'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('log/', views.log, name='page-log'),
]