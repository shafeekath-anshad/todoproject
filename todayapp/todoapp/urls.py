from . import views
from django.urls import path, include
app_name='todayappurl'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name="details"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/', views.update, name="delete"),
]
