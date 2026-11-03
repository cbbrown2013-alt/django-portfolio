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

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

