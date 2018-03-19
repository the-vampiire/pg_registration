from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import CourseLocation, Course, Student
from .register_form import RegistrationForm

import stripe
from pg_site.settings import STRIPE_PUBLISHABLE, STRIPE_SECRET
stripe.api_key = STRIPE_SECRET

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      student = form.save() # save and return the new student
      if student.stripeToken:
        try:
          stripe.Charge.create(
            amount = student.course.price*100, # Stripe payments are in cents
            currency = 'USD',
            description = '%s registration for %s %s' % (str(student.course), student.first_name, student.last_name),
            source = student.stripeToken,
            receipt_email = student.email
          )
          Student.mark_as_paid(student)
        except stripe.CardError as err:
          form.add_error(None, 'Credit card transaction declined')
        # handle payment processing
      return HttpResponseRedirect('success/%d' % (student.pk))

# render registration form view
  context = {
      'form': RegistrationForm(),
      'stripe_publishable': STRIPE_PUBLISHABLE
    }
  return render(request, 'registration/register_student.html', context)
    


def success(request, student_id):
  student = Student.objects.get(id = student_id)
  context = {
    'first': student.first_name,
    'last': student.last_name,
    'course': str(student.course),
    'is_paid': student.is_paid,
    'payment': student.payment_type
  }
  return render(request, 'registration/success.html', context)

