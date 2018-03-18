from django.contrib import admin
from .models import CourseLocation, Course, Student

admin.site.register([CourseLocation, Course, Student])
