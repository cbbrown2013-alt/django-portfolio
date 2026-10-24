#register your models here.

from django.contrib import admin
from .models import Project, Student, Portfolio

admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)
