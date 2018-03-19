from sys import exit
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from .contact_details import ContactDetails
from .course import Course

class Student(ContactDetails):
  class Meta:
    db_table = "students"

  _payment_methods = (
    ("credit", "credit card"),
    ("check", "check"),
    ("po", "purchase order"),
    ("phone", "pay by phone"),
  )

  _reference_types = (
    ("post", "postcard"),
    ("email", "email campaign"),
    ("search", "google"),
    ("rec", "recommendation"),
  )

  first_name = models.CharField(max_length = 20, blank=False)
  last_name = models.CharField(max_length = 25, blank=False)
  email = models.EmailField(blank = False)
  company = models.CharField(max_length = 20, blank=True)
  comments = models.TextField(verbose_name = "registration comments", blank = True)
  is_paid = models.BooleanField(default = False, editable = False)

  course = models.ForeignKey(Course, on_delete = models.CASCADE)
  payment_type = models.CharField(
    max_length = 6,
    choices = _payment_methods,
    blank = False
  )
  reference_type = models.CharField(
    max_length = 6,
    choices = _reference_types,
    blank = False
  )

  def get_stripe_form_details(self):
    return {
      "first": self.first_name,
      "last": self.last_name,
      "street": self.street_address,
      "city": self.city,
      "state": self.state_province,
      "zip": self.zip_code,
      "country": self.country
    }

  @classmethod
  def mark_as_paid(student):
    student.is_paid = True
    student.save()

  def get_absolute_url(self):
    return reverse('registration:success', kwargs = { "id": self.pk }) # used to redirect after a succesful submission

  def __str__(self):
    return "{first} {last} - {email}".format(
      first = self.first_name,
      last = self.last_name,
      email = self.email,
    )




  