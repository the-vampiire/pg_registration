"""
1) define the model class
2) update models/__init__.py to enable model exporting
"""


# https://docs.djangoproject.com/en/2.0/topics/db/models/#fields
from django.db import models
# https://docs.djangoproject.com/en/2.0/ref/validators/#regexvalidator
from django.core.validators import RegexValidator

class CourseLocation(models.Model):
    """
    Represents the location where a course is to be held
    Stores contact information
    """
    class Meta:
        db_table = "course_locations"

    # ID is implicit
    # https://docs.djangoproject.com/en/2.0/topics/db/models/#automatic-primary-key-fields

    name = models.CharField(max_length = 100, blank=False, null=True, unique = True)

    url = models.URLField(max_length = 2000, blank=True, null=True)

    # for the purposes of the MVP this will be a text field
    # https://stackoverflow.com/a/23546819/7542831 for future refactoring ideas
    address = models.TextField(blank=False, null=True)

    # validation for international phone numbers
    # based on E.164 international phone number recommendation
    # https://en.wikipedia.org/wiki/E.164
    phone_validation = RegexValidator(
        regex = r"^\+?\d{8,15}$",
        message = "Enter the phone number using an international format up to 15 digits. e.g. +18135550060 for a US country code (1) and area code (813)"
    )
    phone = models.CharField(max_length = 16, validators = [phone_validation], blank=True, null=True)


    def __str__(self):
        return self.name

