from django.db import models

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

    def __str__(self):
        return self.name
