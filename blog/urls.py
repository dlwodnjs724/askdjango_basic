from django.urls import path
from . import views

app_name = "askdjango"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
]
