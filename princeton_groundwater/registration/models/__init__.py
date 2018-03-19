# modularizing models.py into as a package of models
# https://docs.djangoproject.com/en/2.0/topics/db/models/#organizing-models-in-a-package
from .course_location import CourseLocation
from .course import Course
from .student import Student