from django.urls import path

from core.views import frontpage, gym_d, gym_r

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('gym_d/<slug:slug>/',gym_d,name='detail-gym-d'),
    path('gym_r/<slug:slug>/',gym_r,name='detail-gym-r')

]