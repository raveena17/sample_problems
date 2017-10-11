from __future__ import unicode_literals
from django.db import models
import datetime
# from django.utils.encoding import python_2_unicode_compatible
# from django.utils import timezone


class ClientVisitReport(models.Model):
    prepared_by = models.CharField(max_length=200)#foriegn key to the user
    project_id = models.CharField(max_length=30)  # Should be ForeignKey to project
    project_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    visit_location = models.CharField(max_length=200)
    date_of_visit = models.DateTimeField()
    reason_for_visit = models.TextField(max_length=200)
    action_taken_during_the_visit = models.TextField(max_length=200)
    next_plan_of_action = models.TextField(max_length=200)

    # approved_by should be a ForeignKey to a user
    visit_report_approved_by = models.CharField(max_length=200)
    date_of_approval = models.DateTimeField()

    def __str__(self):
		return self.prepared_by	