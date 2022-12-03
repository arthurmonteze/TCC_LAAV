from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.agend),
    path('info/', views.infoDisp),
    path('disp/<int:id>', views.projView),
    path('newproj/', views.newProj),
]