#This file contains the view functions for the 'portfolio_app' Django application. Views are responsible for handling HTTP requests and returning HTTP responses. They typically retrieve data from the database, process it, and render templates to generate the final HTML output that is sent to the user's browser.

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Portfolio, Student


# Create your views here.

def index(request):
    active_portfolios = Portfolio.objects.filter(is_active=True)
    #Retrieving all active portfolios from the database using the Portfolio model's objects manager. The

    return render(request, 'portfolio_app/index.html', {'active_portfolios': active_portfolios})

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'
    #The StudentListView class is a generic class-based view that inherits from Django's ListView. It is used to display a list of Student objects. The model attribute specifies the model to be used (Student), the template_name attribute specifies the template to render (student_list.html), and the context_object_name attribute defines the name of the context variable that will be used in the template to access the list of students.

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'
    #The StudentDetailView class is a generic class-based view that inherits from Django's DetailView. It is used to display detailed information about a single Student object. The model attribute specifies the model to be used (Student), the template_name attribute specifies the template to render (student_detail.html), and the context_object_name attribute defines the name of the context variable that will be used in the template to access the student object.

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'
    #The PortfolioDetailView class is a generic class-based view that inherits from Django's DetailView. It is used to display detailed information about a single Portfolio object. The model attribute specifies the model to be used (Portfolio), the template_name attribute specifies the template to render (portfolio_detail.html), and the context_object_name attribute defines the name of the context variable that will be used in the template to access the portfolio object.