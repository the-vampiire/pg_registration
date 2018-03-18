# Generated by Django 2.0.2 on 2018-03-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_refactor-inherit_contact_details_on_course_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('pollution', 'The Groundwater Pollution and Hydrology Course'), ('remediation', 'The Groundwater Remediation Course')], max_length=11, null=True)),
                ('price', models.IntegerField(default=1595.0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.CourseLocation')),
            ],
            options={
                'db_table': 'courses',
            },
        ),

# TODO: figure out how to implement cascade since django only "emulates" it
# https://www.fusionbox.com/blog/detail/custom-database-constraints-in-django/594/
        # migrations.RunSQL(
        #     """
        #     set on delete cascade constraint
        #     """
        # )
    ]