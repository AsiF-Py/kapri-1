from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog_list,name='blog'),
    path('<slug>/',views.blog_details),
]