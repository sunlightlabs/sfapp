import json
import urllib
import urllib2

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.views.generic import View

class SubscribeView(View):

	bsd_url = getattr(settings, 'BSD_URL', 'http://bsd.sunlightfoundation.com/page/s/sfc')
	success_message = 'Thanks for registering!'
	
	def get(self, request, *args, **kwargs):
		return HttpResponseNotAllowed(('POST',))

	def post(self, request, *args, **kwargs):

		email = request.POST.get("email", "")
		zipcode = request.POST.get("zipcode", "")

		if email:

			self.bsd_url += "?source=%s" % request.build_absolute_uri()

			params = {"email": email, "zip": zipcode}
			response = urllib2.urlopen(self.bsd_url, urllib.urlencode(params)).read()

		if request.is_ajax():
			resp = {'message': self.success_message}
			return HttpResponse(json.dumps(resp), content_type='application/json')

		messages.success(request, self.success_message)
		referrer = request.META.get('HTTP_REFERER', None)

		return HttpResponseRedirect(referrer or '/')
