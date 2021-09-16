from django.urls import path
from s24 import views


urlpatterns = [
    path('',views.Login,name='login'),
    path('home/',views.home,name='home')
]
