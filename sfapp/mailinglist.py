try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

SUBSCRIBE_URL = 'http://bsd.sunlightfoundation.com/page/s/sfc'
SUCCESS_MESSAGE = 'Thanks for registering!'

def subscribe(email, zipcode, source=None):

    url = SUBSCRIBE_URL

    if source:
        qs = urlencode({'source', source})
        url = '%s?%s' % (url, qs)

    params = {"email": email, "zip": zipcode}
    response = urlopen(url, urlencode(params)).read()

    return response