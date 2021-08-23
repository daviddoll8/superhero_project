from django.urls import path
from . import views

app_name='superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('<int:superhero_id>/', views.detail, name='detail')
]


