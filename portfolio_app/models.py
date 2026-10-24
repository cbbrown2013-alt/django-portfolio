#This file contains the models for the 'portfolio_app' Django application. Models define the structure of the database tables and the relationships between them. Each model corresponds to a table in the database, and each attribute of the model corresponds to a column in that table. The models in this file represent students, their portfolios, and the projects within those portfolios.

#Set up projecct models here.

from django.db import models
from django.db.models import ForeignKey

class Student(models.Model):
    MAJOR = (
        ("CSCI-BS", "BS in Computer Science"),
        ("CPEN-BS", "BS in Computer Engineering"),
        ("BIGD-BI", "BI in Game Design and Development"),
        ("BICS-BI", "BI in Computer Science"),
        ("BISC-BI", "BI in Computer Security"),
        ("CSCI-BA", "BA in Computer Science"),
        ("DASE-BS", "BS in Data Analytics and Systems Engineering"),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField("MSU Email")
    major = models.CharField(max_length=200, choices=MAJOR, blank=True)

    #choices creates a dropdown menu for the major field in the admin panel. The first value is the value stored in the database, and the second value is the human-readable name displayed in the dropdown.

    def __str__(self):
        return self.name

#Returns the student name when the object is printed. This is useful for debugging and for displaying the student name in the admin panel.

class Portfolio(models.Model):
    student = models.OneToOneField( Student, on_delete=models.CASCADE)
    #Creating a one-to-one relationship between the Portfolio and Student models. This means that each student can have only one portfolio, and each portfolio can belong to only one student. The on_delete=models.CASCADE argument specifies that if a student is deleted, their associated portfolio will also be deleted.
    title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title

    #Returns the portfolio title when the object is printed. This is useful for debugging and for displaying the portfolio title in the admin panel.

    def get_absolute_url(self):
        return f"/portfolio/{self.id}/"

    #The get_absolute_url method returns the URL for the portfolio detail page. This is useful for redirecting to the portfolio detail page after creating or updating a portfolio.

class Project(models.Model):
    project = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    #Creating a foreign key relationship between the Project and Portfolio models. This means that each project belongs to a specific portfolio, and each portfolio can have multiple projects. The on_delete=models.CASCADE argument specifies that if a portfolio is deleted, all associated projects will also be deleted.
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    #Returns the project title when the object is printed. This is useful for debugging and for displaying the project title in the admin panel.
    
    def get_absolute_url(self):
        return f"/portfolio/{self.project.id}/project/{self.id}/"

    #The get_absolute_url method returns the URL for the project detail page. This is useful for redirecting to the project detail page after creating or updating a project.