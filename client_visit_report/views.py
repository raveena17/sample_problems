from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
# from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
#from django.views.generic import list_detail
from django.contrib.auth.decorators import permission_required
from django.core.files.uploadedfile import SimpleUploadedFile

from project_management.users.models import UserProfile
from django.contrib.auth.models import User
from project_management.users.forms import UserProfileForm, UserForm, MyProfileForm
from project_management.address.forms import AddressForm
from project_management.announcements.models import Announcement
from project_management.Utility import Email



def manage_myprofile(request):
    """
        Modification of profile of the user.
    """
    profile = request.user.get_profile()
    users_image = profile.users_image
    if not profile:
        raise Http404
    if request.method == 'POST':
        profile_form = MyProfileForm(request.POST, instance = profile)
        address_contact_form = AddressForm(request.POST,
            instance = profile.address_contact, prefix = 'contact')
        address_permanent_form = AddressForm(request.POST,
            instance = profile.address_permanent, prefix = 'permanent')

        if profile_form.is_valid() and address_contact_form.is_valid() \
            and address_permanent_form.is_valid():
            address_contact = address_contact_form.save()
            address_permanent = address_permanent_form.save()

            profile_form.save(address_contact = address_contact,
                address_permanent = address_permanent)
            messages.success(request,
                _('your profile details saved sucessfully'))
    else:
        profile_form = MyProfileForm(instance = profile)
        address_contact_form = AddressForm(instance = profile.address_contact,
            prefix = 'contact')
        address_permanent_form = AddressForm(instance
            = profile.address_permanent, prefix = 'permanent')

    return render(request, 'myprofile.html', {
        'profile_form': profile_form,
        'address_contact_form': address_contact_form,
        'address_permanent_form': address_permanent_form,
        'users_image': users_image
        },
        )# Create your views here.
