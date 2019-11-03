from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anne/', views.anne, name='anne'),
    path('abdi/', views.abdi, name='abdi'),
    path('carolyn/', views.carolyn, name='carolyn'),
    path('ibrahim/', views.ibrahim, name='ibrahim'),
    path('john/', views.john, name='john'),
    path('surabhi/', views.surabhi, name='surabhi'),
    path('tianrong/', views.tianrong, name='tianrong'),
    path('Note1/', views.Note1, name = 'Note1'),
    path('Note2/', views.Note2, name = 'Note2'),
    path('Note3/', views.Note3, name = 'Note3'),
    path('Login/', views.Login, name = 'Login'),
    path('addItem/', views.addItem, name = 'addItem')

]