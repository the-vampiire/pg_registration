from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .models import CourseLocation, Course, Student

class RegisterStudent(CreateView):
    model = Student
    fields = [
      'course',
      'first_name',
      'last_name',
      'street_address',
      'city',
      'state_province',
      'zip_code',
      'country',
      'email',
      'phone',
      'fax',
      'company',
      'payment_type',
      'reference_type',
      'comments'
    ] 

def success(request, id):
  student = Student.objects.get(id = id)
  context = {
    'first': student.first_name,
    'last': student.last_name,
    'course': str(student.course),
    'payment': student.payment_type
  }
  return render(request, 'registration/success.html', context)

