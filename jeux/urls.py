from django.urls import path
from jeux import views
app_name='jeux'
urlpatterns = [
    path('', views.index,name='index'),
    path('add/', views.add,name='add'),
    path('add1/', views.add1,name='add1'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('addgenre/', views.addgenre,name='addgenre'),
]
