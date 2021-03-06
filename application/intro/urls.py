from django.urls import path, include
from . import views

urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path('anne/', views.anne, name='anne'),
    path('abdi/', views.abdi, name='abdi'),
    path('carolyn/', views.carolyn, name='carolyn'),
    path('ibrahim/', views.ibrahim, name='ibrahim'),
    path('john/', views.john, name='john'),
    path('surabhi/', views.surabhi, name='surabhi'),
    path('tianrong/', views.tianrong, name='tianrong'),
    path('Note1/', views.Note1, name='Note1'),
    path('Note2/', views.Note2, name='Note2'),
    path('Note3/', views.Note3, name='Note3'),
    path('main/', views.main_page, name='main'),
    path('addItem/', views.addItem, name='addItem'),
    path('profile/', views.profile_page, name='profile'),
    path('home/', views.home_page, name='home'),
    path('refrigerator/', views.addItem, name='refrigerator'),
    path('shoppingList/', views.shoppingList, name='shoppingList'),
    path('refrigerator/upload', views.searchbar, name='searchbar'),
    path('refrigerator/search/', views.showItems, name='showItems'),
    path('refridgerator/', views.inventory, name='refrigerator'),
    path('removeItem/', views.removeItem, name='removeItem'),
    path('health/', views.healthPage, name='healthPage'),
    path('info/', views.infoPage, name='info'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), #when login page needs to be directly acccessed
]
