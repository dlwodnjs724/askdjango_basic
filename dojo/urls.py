from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'sum/(?P<numbers>[\d/]+)/$', views.mysum),
    # how? path('sum/<str:numbers>/', views.mysum)
    path('hello/<str:name>/<int:age>/', views.hello),
    # re_path(r'hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello)
]
