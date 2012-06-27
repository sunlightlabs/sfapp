# Sunlight Foundation mini-app wrapper

A Flask blueprint is in the works.

## Django

Requires Django >= 1.4

A demo application that displays default styles can be run by:

    python demo.py

### Configuration

settings.py:

    INSTALLED_APPS = (
        ...
        'sfapp',
        ...
    )


urls.py:

    urlpatterns = patterns('',
        ...
        url(r'', include('sfapp.urls')),
        ...
    )

### Templates

To use the provided mini-app templates, extend `sfapp/base-full.html` or `sfapp/base-sidebar.html`.

If the full and sidebar templates do not meet your needs, you can implement your own `sfapp/base-full.html` or `sfapp/base-sidebar.html` within your project. Make sure that your custom versions both extend `sfapp/base.html`.

#### Blocks

The following blocks are provided by the base templates:

container
:    A generic container that holds the content block and, if using the sidebar template, the sidebar block.

content
:    The block that contains your main content. Uses full page width when extending `sfapp/base-full.html`.

sidebar
:    A right-aligned sidebar block is available when extending `sfapp/base-sidebar.html`. To customize the placement or width of this block, implement a custom `sfapp/base-sidebar.html`.

title
:    Title of the page

og
:    Open Graph meta elements

css
:    link and style elements for CSS

js
:    script elements for JavaScript (included at the end of the document)

head
:    Miscellaneous meta and other elements that belong in head

ga
:    Google analytics code (not the JavaScript, just the tracking ID)

bodyclass
:    The content of the class attribute on the body element.

### Mailing List Signup Form

By default, the form will be submitted to the Sunlight Foundation generic mailing list. To use an app-specific mailing list, set `BSD_URL` in `settings.py`.

    BSD_URL = "http://bsd.sunlightfoundation.com/page/signup/Public_Markup"

`sfapp.urls` contains a URL config that will handle form submissions to `/subscribe/`. You can use a different URL by overriding the URL config in your own `urls.py`. You can also customize the view by inheriting `SubscribeView`:

    from sfapp.views import SubscribeView

    class MySubscribeView(SubscribeView):
        bsd_url = "http://bsd.sunlightfoundation.com/page/signup/Public_Markup"
        success_message = "High five! You've been registered."

    urlpatterns = patterns('',
        ...
        url(r'^subscribe/$', MySubscribeView.as_view()),
        ...
    )

The following attributes are available on `SubscribeView`:

bsd_url
:    Defaults to `settings.BSD_URL` or the default Sunlight Foundation mailing list

success_message
:    The message that will be displayed to the user on successful registration

The provided base template includes JavaScript that will do a fancy Ajax form submission.