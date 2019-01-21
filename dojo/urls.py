from django.urls import path, re_path
from . import views

urlpatterns = [
    path('sum/<int:x>/', views.mysum),
    path('sum/<int:x>/<int:y>/', views.mysum),
    path('sum/<int:x>/<int:y>/<int:z>/', views.mysum),
     # re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum)
]
