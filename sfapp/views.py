import json
import urllib
import urllib2

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.views.generic import View

from sfapp import mailinglist

class SubscribeView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(('POST',))

    def post(self, request, *args, **kwargs):

        email = request.POST.get("email", "")
        zipcode = request.POST.get("zipcode", "")

        if email:

            response = mailinglist.subscribe(email, zipcode)

        if request.is_ajax():
            resp = {'message': mailinglist.SUCCESS_MESSAGE}
            return HttpResponse(json.dumps(resp), content_type='application/json')

        messages.success(request, mailinglist.SUCCESS_MESSAGE)
        referrer = request.META.get('HTTP_REFERER', None)

        return HttpResponseRedirect(referrer or '/')
