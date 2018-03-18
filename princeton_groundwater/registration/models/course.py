from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from .course_location import CourseLocation

class Course(models.Model):
  class Meta:
    db_table = "courses"

  # TODO: find a way to turn this into an Admin editable enum
  course_options = (
    ("pollution", "The Groundwater Pollution and Hydrology Course"),
    ("remediation", "The Groundwater Remediation Course")
  )

  # FK for Course Location
  course_location = models.ForeignKey(CourseLocation, on_delete = models.CASCADE)

  title = models.CharField(max_length = 11, choices = course_options, blank=False, null=True)
  price = models.IntegerField(default = 1595.00)
  start_date = models.DateField(blank = False) # TODO: do not allow blank
  end_date = models.DateField(blank = False)

  def __str__(self):
    return "{title} - {start}".format(title = self.title, start = self.start_date)

  def print_details(self):
    return """
    Course Title: {title}
    Price: ${price}
    Start Date: {start}
    End Date: {end}

{location_details}
    """.format(
      title = self.title,
      price = self.price,
      start = self.start_date,
      end = self.end_date,
      location_details = CourseLocation.objects.get(id = self.course_location).print_details()
    )
