import os, sys
sys.path.append('/home/linuxadmin/projects/payit')
sys.path.append('/home/linuxadmin/projects/payit/apps/project_management')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_management.settings'
import django.core.handlers.wsgi
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
application = django.core.handlers.wsgi.WSGIHandler()

