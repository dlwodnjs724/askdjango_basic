from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'sum/(?P<numbers>[\d/]+)/$', views.mysum),
    # how? path('sum/<str:numbers>/', views.mysum)
]
