from django.urls import include, path
from . import views

urlpatterns = [
    #geral
    path('', views.agend),
    path('info/', views.infoDisp),
    path('prof/', views.prof),
    #dispositivo
    path('disp/<int:id>', views.projView),
    path('newdisp/', views.newDisp),
    path('editdisp/<int:id>', views.editDisp),
    path('deletedisp/<int:id>', views.deleteDisp),
    #professor
    path('prof/<int:id>', views.profView),
    path('newprof/', views.newProf),
    path('editprof/<int:id>', views.editProf),
    path('deleteprof/<int:id>', views.deleteProf),
]