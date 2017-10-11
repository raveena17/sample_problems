# from django.conf.urls.defaults import patterns
from django.conf.urls import include, url

from django.views.generic import TemplateView
from django.views.generic import RedirectView
from project_management.client_visit_report import views as client_visit_report_views

urlpatterns = [
    url(r'^cvr/$', 'client_visit_report_views.manage_cvr'),
    
]
