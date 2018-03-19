from django.forms import ModelForm, CharField
from .models import Student

class RegistrationForm(ModelForm):
  class Meta:
    model = Student

    fields = (
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
      'reference_type',
      'comments',
      'payment_type',
      'stripeToken'
    )

  # override to inject bootstrap class
  # https://stackoverflow.com/a/31627454/7542831
  def __init__(self, *args, **kwargs):
    super(RegistrationForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({ 'class': 'form-control' })
