"""
Url pattern for Reimbursement application
"""

# from django.conf.urls.defaults import *
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from project_management.reimbursement import views as reimbursement_views


uuid_regex = '[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

urlpatterns = [
    url(r'^create/$', 'reimbursement_views.create',name="create"),
    url(r'^list/$', 'reimbursement_views.list',name="list"),
    url(r'^save/$', 'reimbursement_views.save',name="save"),    
]
