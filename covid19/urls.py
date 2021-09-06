from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-date-info', views.get_date_info, name='get_date_info'),
    path('get-state-info', views.get_state_info, name='get_state_info'),
    path('pinpoint-state', views.pinpoint_state, name='pinpoint_state')
]