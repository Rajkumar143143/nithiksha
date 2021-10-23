from . import views
from django.urls import path

app_name = 'homepage'
urlpatterns = [
    # /homepage/
    path('', views.index, name='index'),
    # /home/2
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    ]