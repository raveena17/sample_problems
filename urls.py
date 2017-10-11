from django.conf import settings
from django.contrib.auth.decorators import login_required
# from django.conf.urls.defaults import *
# from django.conf.urls import url, include
from django.views.generic.list import ListView
#from django.conf.urls import *
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout

# from django.views.generic import list_detail
# from django.views.generic.simple import TemplateView.as_view RedirectView
from django.views.generic import TemplateView
from django.views.generic import RedirectView

from project_management.users.models import UserProfile
from project_management.users.views import login
from django.contrib.auth import views as auth_views

from project_management.projectbudget.models import *
from project_management.projectbudget.budgetmasters import *
from django.conf.urls import include, url

import os.path
import django_cron

admin.autodiscover()

try:
    django_cron.autodiscover()
except BaseException:
    pass


from project_management.common_manager import views as common_manager_views
# from project_management.logs import views as logs_views
from project_management.logs.views import DisplayLog, DisplayLogData, GetLog
# from project_management.notifications import eventviews as notifications_eventviews
from project_management.notifications.eventviews import *
from project_management.repository.views import *
from project_management.non_project_task.views import *
from project_management.Utility import getPopUpDetails
from project_management.common_manager.views import *




from project_management.projects import views as projects_views
from project_management.repository import views as repository_views
from project_management.non_project_task import views as non_project_task_views
# from django.core.context_processors import csrf
from django.views.i18n import *
# from project_management.i18nDate import javascript_catalog

# for the calender(datepicker) widget
# urlpatterns = [
#     url(r'^jsi18n/$','project_management.i18nDate.javascript_catalog',{'packages': 'django.conf'}),
# ]


js_info_dict = {'packages': ('cui.translations',), }

# urlpatterns.append = [
#     url(r'^django-jsi18n/$',django.views.i18n.javascript_catalog, js_info_dict),

   
# ]
                        

urlpatterns = [
    url(r'^django-jsi18n/$',javascript_catalog, js_info_dict),
    # url(r'^jsi18n/$',javascript_catalog,{'packages': 'django.conf'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^comingsoon/$', TemplateView.as_view(template_name = 'coming_soon.html')),
    url(r'^recentupdates/$', TemplateView.as_view(template_name = 'Recent_updates.html')),
    url(r'^re-use/$', TemplateView.as_view(template_name = 're-use.html')),
    url(r'^re-use/components/$', TemplateView.as_view(template_name = 'Re-Use_Library.html')),
    url(r'^5GPal/$', TemplateView.as_view(template_name = '5G-Pal.html')),
    url(r'^5GPal/Policies/$', TemplateView.as_view(template_name = '5gpal_Policies.html')),
    url(r'^5GPal/FxCop_and_Rules/$', TemplateView.as_view(template_name = '5gpal_FxCop_and_Rules.html')),
    url(r'^5GPal/Process-templates/$', TemplateView.as_view(template_name = '5gpal__process-templates.html')),
    url(r'^Mindshare/', RedirectView, {'url': '/login/'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    # url(r'^contacts/$', login_required.as_view(),{'queryset': UserProfile.objects.exclude(user__is_active=False).exclude(
    #                          user__is_staff=True).order_by('user__username'),
    #                         'template_name': 'contacts.html'}),
    url(r'^contacts/$', login_required(TemplateView.as_view(template_name='contacts.html'))),
    
    url(r'^Logs/', DisplayLog),
    url(r'^admin.ShowLog/', DisplayLogData),
    url(r'^GetLogDetail/',GetLog),
    url(r'^user/', include('project_management.users.urls')),
    url(r'^project/', include('project_management.projects.urls')),
    url(r'^projectbudget/', include('project_management.projectbudget.urls')),
    url(r'^alert/', include('project_management.alert.urls')),
    url(r'^customer/', include('project_management.customer.urls')),
    url(r'^task/', include('project_management.tasks.urls')),
    url(r'^milestone/', include('project_management.milestone.urls')),
    url(r'^businessunit/', include('project_management.business_unit.urls')),
    url(r'^event/', include('project_management.notifications.urls')),
    url(r'^announcement/', include('announcements.urls')),

    # url(r'^client_visit_report/', include('project_management.client_visit_report.urls')),

    url(r'^timesheet/', include('project_management.timesheet.urls')),
    url(r'^timesheetnew/', include('project_management.timesheetnew.urls')),
    url(r'^NewsLetter/', include('newsletter.urls')),
    url(r'^conferenceroombooking/', include('project_management.conferenceroombooking.urls')),
    url(r'^codereview/', include('project_management.code_review.urls')),

    # url(r'^codereview/', include('project_management.code_review.urls', urlnamespace="codereview")),
    #url(r'^library/',include('project_management.library.urls')),
    # url(r'^comments/', include('comments.urls', namespace='comments')),

    url(r'^MonthlyCalendar/$', MonthlyCalendar),
    url(r'^WeeklyCalendar/$', WeeklyCalendar),
    url(r'^DayCalendar/$', DayCalendar),
    url(r'^previousyear/(?P<type>\w+)/', previousyear),
    url(r'^nextyear/(?P<type>\w+)/', nextyear),
    url(r'^previousmonth/', previousmonth),
    url(r'^nextmonth/', nextmonth),
    url(r'^nextday/', nextday),
    url(r'^previousday/', previousday),
    url(r'^nextweek/', nextweek),
    url(r'^previousweek/', previousweek),
    url(r'^Event/', Events),
    url(r'^CreateEvent/', Events),
    url(r'^SaveEvent/', saveEvent),
    url(r'^Eventdelete/', eventDelete),
    url(r'^UpdateEvent/', updateEvent),
    url(r'^EventAccess/', accessEvent),
    url(r'^GetStage/', getStage),

    url(r'^prog_task_in_pg/$', TemplateView.as_view(template_name = "prog_task_in_pg.html"), name="prog_task_in_pg"),
    url(r'^repository/', RepositoryView),
    url(r'^repositoryUpload/', RepositoryUpload),
    url(r'^SaveNonProjectTask/', SaveNonProjectTask),
    url(r'^SaveAndContinueNonProjectTask/', SaveAndContinueNonProjectTask),
    url(r'^GetPopUpDetails/', getPopUpDetails),
    url(r'^MasterView/', MasterView),
    url(r'^MasterSave/', MasterSave),
    url(r'^MasterDelete/', MasterDelete),

]












# to load the static data
# if settings.DEBUG:
# urlpatterns.append = [
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT, "media")}),
# ]


# urlpatterns.append = [
#     # url(r'^Logs/', 'logs_views.DisplayLog'),
#     # url(r'^admin.ShowLog/', 'logs_views.DisplayLogData'),
#     # url(r'^GetLogDetail/', 'logs_views.GetLog'),
#     url(r'^Logs/', DisplayLog),
#     url(r'^admin.ShowLog/', DisplayLogData),
#     url(r'^GetLogDetail/',GetLog),
# ]


# urlpatterns.append = [
#     url(r'^user/', include('project_management.users.urls')),
#     url(r'^project/', include('project_management.projects.urls')),
#     url(r'^projectbudget/', include('project_management.projectbudget.urls')),
#     url(r'^alert/', include('project_management.alert.urls')),
#     url(r'^customer/', include('project_management.customer.urls')),
#     url(r'^task/', include('project_management.tasks.urls')),
#     url(r'^milestone/', include('project_management.milestone.urls')),
#     url(r'^businessunit/', include('project_management.business_unit.urls')),
#     url(r'^event/', include('project_management.notifications.urls')),
#     url(r'^announcement/', include('announcements.urls')),

#     # url(r'^client_visit_report/', include('project_management.client_visit_report.urls')),

#     url(r'^timesheet/', include('project_management.timesheet.urls')),
#     url(r'^timesheetnew/', include('project_management.timesheetnew.urls')),
#     url(r'^NewsLetter/', include('newsletter.urls')),
#     url(r'^conferenceroombooking/', include('project_management.conferenceroombooking.urls')),
#     url(r'^codereview/', include('project_management.code_review.urls', urlnamespace="codereview")),
#     #url(r'^library/',include('project_management.library.urls')),
# ]


# urlpatterns.append = [
#     url(r'^MonthlyCalendar/$', 'notifications_eventviews.MonthlyCalendar'),
#     url(r'^WeeklyCalendar/$', 'notifications_eventviews.WeeklyCalendar'),
#     url(r'^DayCalendar/$', 'notifications_eventviews.DayCalendar'),
#     url(r'^previousyear/(?P<type>\w+)/', 'notifications_eventviews.previousyear'),
#     url(r'^nextyear/(?P<type>\w+)/', 'notifications_eventviews.nextyear'),
#     url(r'^previousmonth/', 'notifications_eventviews.previousmonth'),
#     url(r'^nextmonth/', 'notifications_eventviews.nextmonth'),
#     url(r'^nextday/', 'notifications_eventviews.nextday'),
#     url(r'^previousday/', 'notifications_eventviews.previousday'),
#     url(r'^nextweek/', 'notifications_eventviews.nextweek'),
#     url(r'^previousweek/', 'notifications_eventviews.previousweek'),
#     url(r'^Event/', 'notifications_eventviews.Events'),
#     url(r'^CreateEvent/', 'notifications_eventviews.Events'),
#     url(r'^SaveEvent/', 'notifications_eventviews.saveEvent'),
#     url(r'^Eventdelete/', 'notifications_eventviews.eventDelete'),
#     url(r'^UpdateEvent/', 'notifications_eventviews.updateEvent'),
#     url(r'^EventAccess/', 'notifications_eventviews.accessEvent'),
#     url(r'^GetStage/', 'notifications_eventviews.getStage'),
# ]

#  Program Task (Internal Tab) URL's
# urlpatterns.append = [
#     url(r'^prog_task_in_pg/$', TemplateView.as_view(template = "prog_task_in_pg.html"), name="prog_task_in_pg"),
#     #url(r'^UpdateProgramTask/', 'ProgTaskListsViews.program_task_update_pg'),
#     #url(r'^CreateProgramTask/', 'ProgTaskListsViews.createprogramtask'),
#     #url(r'^CreateContinueProgramTask/', 'ProgTaskListsViews.createandcontinueprogramtask'),
#     #url(r'^prog_task_up/', 'ProgTaskListsViews.program_task_update'),
# ]

# urlpatterns.append = [
#     url(r'^repository/', RepositoryView),
#     url(r'^repositoryUpload/', RepositoryUpload),
# ]


# urlpatterns.append = [#'project_management.non_project_task',
#     #url(r'^CreateMenuTask/', 'createMenuTaskViews.CreateMenuTaskView'),
#     #url(r'^GetProjectTasklists/', 'createMenuTaskViews.GetTasklists'),
#     #url(r'^GetProjectTasklistsResources/','createMenuTaskViews.GetTasklistsResources'),
#     #url(r'^SaveCreateMenuTask/', 'createMenuTaskViews.CreateMenuTaskSave'),
#     #url(r'^SaveAndContinueCreateMenuTask/', 'createMenuTaskViews.CreateMenuTaskSaveAndContinue'),
# ]

# urlpatterns.append = [
#     #url(r'^NonProjectTaskList/', 'NonProjectTaskList'),
#     #url(r'^CreateNonProjectTask/', 'NonProjectTaskView'),
#     #url(r'^UpdateNonProjectTask/', 'NonProjectTaskView'),
#     url(r'^SaveNonProjectTask/', 'non_project_task_views.SaveNonProjectTask'),
#     url(r'^SaveAndContinueNonProjectTask/', 'non_project_task_views.SaveAndContinueNonProjectTask'),
#     #url(r'^NonProjectTaskdelete/', 'NonProjectTaskDelete'),
# ]

# urlpatterns.append = [
#     url(r'^GetPopUpDetails/', 'project_management.Utility.getPopUpDetails'),
# ]


# urlpatterns.append = [
#     url(r'^MasterView/', 'common_manager_views.MasterView'),
#     url(r'^MasterSave/', 'common_manager_views.MasterSave'),
#     url(r'^MasterDelete/', 'common_manager_views.MasterDelete'),
# ]

# urlpatterns = ['project_management.projectbudget.views',
#                      url(r'^projectbudget/$', 'projectbudget.views.cost'),
#                    ]
