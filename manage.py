#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # When you use Django, you have to tell it which settings you're using. Do this by using an environment variable.


    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yanyi.settings')

    # if you wanno do that,you mush
    #       export DJANGO_SETTINGS_MODULE=mysite.settings
    #       django-admin runserver
    #  OR
    #       django-admin runserver --settings=mysite.settings

    # In some cases, you might want to bypass the DJANGO_SETTINGS_MODULE environment variable.
    # In these cases, you can configure Django's settings manually.
    # Do this by calling:  django.conf.settings.configure(default_settings, **settings)
    #       from django.conf import settings
    #       settings.configure(DEBUG=True)

    # Custom default settings
    # If you'd like default values to come from somewhere other than django.conf.global_settings,
    # you can pass in a module or class that provides the default settings as the default_settings argument
    #       from django.conf import settings
    #       from myapp import myapp_defaults
    #       settings.configure(default_settings=myapp_defaults, DEBUG=True)

    # warn:
    # If you're not setting the DJANGO_SETTINGS_MODULE environment variable, you must call configure() at some point before using any code that reads settings.
    # If you don't set DJANGO_SETTINGS_MODULE and don't call configure(), Django will raise an ImportError exception the first time a setting is accessed.
    # If you set DJANGO_SETTINGS_MODULE, access settings values somehow, then call configure(), Django will raise a RuntimeError indicating that settings have already been configured.
    # Also, it's an error to call configure() more than once, or to call configure() after any setting has been accessed.  tip: settings.configured -- bool

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
