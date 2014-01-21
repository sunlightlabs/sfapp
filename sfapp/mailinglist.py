import urllib
import urllib2

SUBSCRIBE_URL = 'http://bsd.sunlightfoundation.com/page/s/sfc'
SUCCESS_MESSAGE = 'Thanks for registering!'

def subscribe(email, zipcode, source=None):

    url = SUBSCRIBE_URL

    if source:
        qs = urllib.urlencode({'source', source})
        url = '%s?%s' % (url, qs)

    params = {"email": email, "zip": zipcode}
    response = urllib2.urlopen(url, urllib.urlencode(params)).read()

    return response