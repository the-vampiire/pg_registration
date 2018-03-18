from sys import exit
from django.db import models
from django.core.exceptions import ValidationError
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

  _reference_type = (
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
  is_paid = models.BooleanField(default = False)

  course = models.ForeignKey(Course, on_delete = models.CASCADE)
  payment_type = models.CharField(
    max_length = 6,
    choices = _payment_methods,
    blank = False
  )
  reference_type = models.CharField(
    max_length = 6,
    choices = _reference_type,
    blank = False
  )

  def _mark_as_paid(self):
    self.is_paid = True
    self.save()

  def __str__(self):
    return "{first} {last} - {email}".format(
      first = self.first_name,
      last = self.last_name,
      email = self.email,
    )








  