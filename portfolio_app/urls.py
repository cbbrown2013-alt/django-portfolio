# URL configuration for the portfolio_app.


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


