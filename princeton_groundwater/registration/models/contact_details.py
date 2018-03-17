# abstract base models for Django
# https://godjango.com/blog/django-abstract-base-class-model-inheritance/

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

#TODO: consider moving Contact Details to its own table
# store FK on Student and Coure Location tables
class ContactDetails(models.Model):
  """
  Stores contact information for a student or course location
  Optional fields: zip, phone number, fax number
  """
  class Meta:
    abstract = True # Django will not treat this model as a table
  
  street_address = models.CharField(max_length = 100, blank=False, null=True)
  city = models.CharField(max_length = 50, blank=False, null=True)
  zip_code = models.CharField(max_length = 5, blank=True, null=True) # optional
  state_province = models.CharField(max_length = 50, blank=False, null=True)
  country = models.CharField(max_length = 50, blank=False, null=True)

  # validation for international phone numbers
  # based on E.164 international phone number recommendation
  # https://en.wikipedia.org/wiki/E.164
  phone_validation = RegexValidator(
      regex = r"^\+?\d{8,15}$",
      message = "Must enter the phone number using an international format up to 15 digits. e.g. +18135550060 for a US country code (1) and area code (813)"
  )
  phone = models.CharField(max_length = 16, validators = [phone_validation], blank=True, null=True)
  fax = models.CharField(max_length = 16, validators = [phone_validation], blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

# TODO: add form validation when creating the Form

  # ensure either phone or email are passed
  # https://stackoverflow.com/a/23434418/7542831
  def clean(self):
    cleaned_data = super(ContactDetails, self).clean() # call Django default clean first
    if not self.phone and not self.email:
      raise ValidationError({"contact_detail": "Must provide either a phone number or email address"})
    return cleaned_data # if above validation passes return the default cleaned data
  
  # full_clean() is not called by default in the Django model save() method
  # call to trigger the self.clean() method and provide the above validation
  # https://docs.djangoproject.com/en/2.0/ref/models/instances/#validating-objects
  def save(self, *args, **kwargs):
    self.full_clean()
    return super(ContactDetails, self).save(*args, **kwargs)

  def __str__(self):
    return """
Location
    Street: {street}
    City: {city}
    State/Province: {state}
    Zip Code: {zip}
    Country: {country}

Contact
    Email: {email}
    Phone Number: {phone}
    Fax Number: {fax}
    """.format(
      street = self.street_address,
      city = self.city,
      state = self.state_province,
      zip = self.zip_code if hasattr(self, 'zip_code') else 'no zip code provided',
      country = self.country,
      email = self.email if hasattr(self, 'email') else 'no email provided',
      phone = self.phone if hasattr(self, 'phone') else 'no phone number provided',
      fax = self.fax if hasattr(self, 'fax') else 'no fax number provided'
    )