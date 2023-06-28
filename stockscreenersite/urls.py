from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('<str:slug>-stock-financial-information/', views.stock_detail, name='stock_detail'),
    path('stock-screener', views.stock_screener, name='stock_screener'),
]
