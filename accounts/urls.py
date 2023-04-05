
from django.contrib import admin
from django.urls import path, include   
from rest_framework.authtoken import views
from new_users.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('new_users.urls')),
    path('login/', include('dj_rest_auth.urls')),
    path('loginemail/', LoginEmailView.as_view() ),
    path('loginnumber/', LoginNumberView.as_view()),
    path('api-token-auth', views.obtain_auth_token)
]
