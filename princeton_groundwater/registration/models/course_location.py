# https://docs.djangoproject.com/en/2.0/topics/db/models/#fields
from .contact_details import ContactDetails
# https://docs.djangoproject.com/en/2.0/ref/validators/#regexvalidator
from django.core.validators import RegexValidator
from django.db import models

class CourseLocation(ContactDetails): # inherits models.Model as grandparent class
    """
    Represents the location where a course is to be held
    Stores contact information inherited from ContactDetails abstract class
    inherits Django Models class as grandparent class through ContactDetails
    """
    class Meta:
        db_table = "course_locations" # renames from registration_* to course_locations

    # ID is implicit
    # https://docs.djangoproject.com/en/2.0/topics/db/models/#automatic-primary-key-fields
    name = models.CharField(max_length = 100, blank=False, null=True, unique = True)
    url = models.URLField(max_length = 2000, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def print_details(self):
        return super(ContactDetails, self).__str__()

