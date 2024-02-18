from django.urls import path
from . import views
urlpatterns = [
    path('rj/',views.rj_list,name='rj_list'),
    path('rj/<int:id>/',views.rj_details,name='rj_details'),
    path('<int:id>/',views.show_details,name='show_details'),
    path('show-schedule/',views.show_schedule,name='show_schedule'),

]