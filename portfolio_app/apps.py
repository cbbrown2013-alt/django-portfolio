#This file defines the configuration for the 'portfolio_app' Django application. The AppConfig class is used to configure some of the attributes of the application, such as its name. This configuration is necessary for Django to recognize and manage the application correctly within the project.

from django.apps import AppConfig


class PortfolioAppConfig(AppConfig):
    name = 'portfolio_app'

#Context: This is the configuration class for the portfolio_app Django application. It specifies the name of the application, which is used by Django to identify and manage the app.