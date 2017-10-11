from django.conf import settings
from django.contrib.auth.models import UserManager
from django.core.mail import EmailMessage
# from django.core.mail import SMTPConnection
from django.core.mail import get_connection

from django.db.models.query import QuerySet
from django.core import mail
#from project_management.users.models import FiveGUser

from datetime import datetime
import os
import uuid

class Util:

    def __init__(self):
        return

    def Guid(self):
        uniqueId = str(uuid.uuid4())
        return uniqueId[:36]

    def GeneratePassword(self):
        return UserManager().make_random_password(length =  8,
            allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')


class Email:

    def __init__(self):
        return

    def send_email(self, subject, message, recipients, contenttype = 'plain',response = None, attach = ''):
        try:            
            from settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
        finally:
            if(EMAIL_HOST_USER != ''):
                from_email = EMAIL_HOST_USER
            connection = mail.get_connection()
            connection.open() 
            emailMessage = EmailMessage(subject, message, from_email, recipients)
            emailMessage.content_subtype = contenttype
            if attach.strip() != '':
                emailMessage.attach_file(attach)
            connection.send_messages([emailMessage])
            connection.close()


    # def send_email(self, subject, message, recipients, contenttype = 'plain',response = None, attach = ''):
    #     connection = get_connection( 
    #         username = auth_user,
    #         password = auth_password,
    #         fail_silently = fail_silently,
    # ))
    #     emailMessage = EmailMessage(subject, message, from_email, recipients_list, connection = connection)
    #         subject,
    #         message, 
    #         settings.EMAIL_HOST_USER, 
    #         recipients,
    #         connection = connection,
    #     )
    #     emailMessage.send()
    #     connection.close()

    #     emailMessage.content_subtype = contenttype
    #     if attach.strip() != '':
    #         emailMessage.attach_file(attach)
    #     connection.send_messages([emailMessage])



    # def send_email(self, subject, message, recipients, contenttype = 'plain',response = None, attach = ''):
    #     connection = SMTPConnection(settings.EMAIL_HOST, settings.EMAIL_PORT,
    #         settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD,
    #         settings.EMAIL_USE_TLS)
    #     emailMessage = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipients)
    #     emailMessage.content_subtype = contenttype
    #     if attach.strip() != '':
    #         emailMessage.attach_file(attach)
    #     connection.send_messages([emailMessage])



        
class EmailWithCC:
    def __init__(self):
        return

    def send_email(self, subject, message, recipients, contenttype='plain', attach='', from_email='', copyc=''):       
        try:            
            from settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
        finally:
            if(EMAIL_HOST_USER != ''):
                from_email = EMAIL_HOST_USER
            #import pdb;pdb.set_trace()
            connection = mail.get_connection()
            # Manually open the connection
            connection.open()            
            if(copyc != '' and len(copyc) > 0):
                emailMessage = EmailMessage(subject, message, from_email, recipients, cc=copyc)
            else:
                emailMessage = EmailMessage(subject, message, from_email, recipients)
            emailMessage.content_subtype = contenttype
            if attach.strip() != '':
                emailMessage.attach_file(attach)
            connection.send_messages([emailMessage])
            # We need to manually close the connection.
            connection.close()
            
#"""
#def IsUserExecutive( request ):
#    return request.session.get('loginUserPrivilege','') == 'Executive'
#"""

def GetDateType( dateString, format = None ):
    if(format==None):
        format = settings.DATE_FORMAT
        format = format.replace('d','%d')
        format = format.replace('m','%m')
        format = format.replace('Y','%Y')
    try:
        return datetime.strptime( dateString, format ).date()
    except:
        return datetime.strptime( '2000-01-01', "%Y-%m-%d" ).date()

def GetLocalDate(request):
    LoginData = request.session.get('LoginData','')
    localDate = datetime.date(datetime.today())
    if LoginData != '':
        localDate = GetDateType(LoginData['localDate'],"%Y-%m-%d")
    return localDate

def flatten(lst):
    for elem in lst:
        if type(elem) in (tuple, list, QuerySet):
            for i in flatten(elem):
                yield i
        else:
            yield elem

def ChangeMode(dirname, name = None):
    dirmode = 777
    flmode = 777
    if os.path.isdir(dirname):
        os.system('chmod %d "%s"' % (dirmode, dirname))
        os.system('chmod %d "%s"' % (dirmode, dirname))
        # os.chmod(fl, dirmode)   # <--- Does not work
    if name != None:
        name = os.path.join(dirname, name)
        if os.path.isfile(name):
            os.system('chmod %d "%s"' % (flmode, name))
            # os.chmod(fl, flmode)    # <--- Does not work

def GetLoginUserName(request):
    userName = ''
    LoginData = request.session.get('LoginData', '')
    if LoginData != '':
        userName = LoginData['userName'][0]
    return userName

def getUserTypeFilter(attendees, usertype = 'both'):
    #TODO: since we coud'nt sort the dict below query is done
    SORTING_KEY = '007'
    #fivegQuery = FiveGUser.objects.filter(pk = SORTING_KEY)
    fivegQuery = User.objects.exclude(is_active = '0', is_staff = '1')
    return fivegQuery, []

def getPopUpDetails(request):
    from django.http import HttpResponse
    # from django.utils import simplejson
    try:
        import django.utils.simplejson
    except:
        import json as simplejson

    userid = request.GET.get('user','')
    #items = FiveGUser.objects.filter(userID = userid)
    items = User.objects.filter(id = userid)
    if (len(items)) <= 0:
        return
    item = [{'name': each.first_name + each.last_name, 'id':each.pk, 'title':each.title,
            #'email': each.email, 'role': each.userProfile.role.name,
            #'office': each.userProfile.officeNumber, 'extn': each.userProfile.extensionNumber,
            #'mobile': each.userProfile.mobile, 'notes': each.notes
            }
            for each in items]
    json = simplejson.dumps(item)
    return HttpResponse(json, mimetype='application/javascript')
