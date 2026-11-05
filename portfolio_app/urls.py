# URL configuration for the portfolio_app.


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #The urlpatterns list defines the URL patterns for the portfolio_app Django application. Each path() function maps a specific URL pattern to a corresponding view function or class-based view. The name parameter allows for easy reference to these URLs in templates and other parts of the application.
    path('students/', views.StudentListView.as_view(), name='student-list'),
    #The path() function for the 'students/' URL pattern maps to the StudentListView class-based view. The as_view() method is called to convert the class into a view function that can handle HTTP requests. The name parameter 'student-list' allows for easy reference to this URL in templates and other parts of the application.
    path( 'students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    #The path() function for the 'students/<int:pk>/' URL pattern maps to the StudentDetailView class-based view. The <int:pk> part of the URL captures an integer value from the URL and passes it as a keyword argument named pk to the view. This allows the view to retrieve and display detailed information about a specific Student object based on its primary key (pk). The name parameter 'student-detail' allows for easy reference to this URL in templates and other parts of the application.
    path('portfolios/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    #The path() function for the 'portfolios/<int:pk>/' URL pattern maps to the PortfolioDetailView class-based view. Similar to the previous URL pattern, the <int:pk> part captures an integer value from the URL and passes it as a keyword argument named pk to the view. This allows the view to retrieve and display detailed information about a specific Portfolio object based on its primary key (pk). The name parameter 'portfolio-detail' allows for easy reference to this URL in templates and other parts of the application.
]


