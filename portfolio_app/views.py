#This file contains the view functions for the 'portfolio_app' Django application. Views are responsible for handling HTTP requests and returning HTTP responses. They typically retrieve data from the database, process it, and render templates to generate the final HTML output that is sent to the user's browser.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # This view function handles requests to the index page of the portfolio app.
    # It renders the 'index.html' template and returns it as an HTTP response.
    return render(request, 'portfolio_app/index.html')
    # The 'render' function takes the request object, the template name, and an optional context dictionary (not used here) to generate the final HTML response.