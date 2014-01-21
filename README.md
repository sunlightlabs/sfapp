# Sunlight Foundation mini-app wrapper

Templates and helpers for Django and Flask. Built on Bootstrap 3.

A demo application that displays default styles can be run with `python demo_flask.py` for Flask or `python demo_django.py` for Django.

## Configuration

### Django

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

### Flask

In your app:

    from sfapp.blueprint import sfapp
    app.register_blueprint(sfapp)

## Templates

To use the provided mini-app templates, extend `sfapp/<framework>/base-full.html` or `sfapp/<framework>/base-sidebar.html`. `<framework>` must be one of `django` or `flask`.

If the full and sidebar templates do not meet your needs, you can implement your own `sfapp/<framework>/base-full.html` or `sfapp/<framework>/base-sidebar.html` within your project. Make sure that your custom versions both extend `sfapp/<framework>/base.html`.

### Blocks

The following blocks are provided by the base templates:

container
:    A generic container that holds the content block and, if using the sidebar template, the sidebar block.

content
:    The block that contains your main content. Uses full page width when extending `sfapp/<framework>/base-full.html`.

sidebar
:    A right-aligned sidebar block is available when extending `sfapp/<framework>/base-sidebar.html`. To customize the placement or width of this block, implement a custom `sfapp/<framework>/base-sidebar.html`.

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

## Mailing List Signup Form

The provided base template includes JavaScript that will do a fancy Ajax form submission and attempt to subscribe to the Sunlight Foundation mailing list. The route is mounted at */subscribe*.

Subscriptions for both frameworks are handled by the *sfapp.mailinglist* module. *subscribe(email, zipcode, source=None)* is the method that will invoke the subscription endpoint and return the response.

### Django

`sfapp.urls` contains a URL config that will handle form submissions to `/subscribe/`. You can use a different URL by overriding the URL config in your own `urls.py`. You can also customize the view by inheriting `SubscribeView`:

    from sfapp.views import SubscribeView

    class MySubscribeView(SubscribeView):
        pass # do something here

    urlpatterns = patterns('',
        ...
        url(r'^subscribe/$', MySubscribeView.as_view()),
        ...
    )

### Flask

No customizations yet.