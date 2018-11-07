"""yanyi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# This module is pure Python code and is a mapping between URL path expressions to Python functions (your views).


from django.contrib import admin
from django.urls import path, include


# How Django processes a request
#   1. Django determines the root URLconf module to use.
#      Ordinarily, this is the value of the ROOT_URLCONF setting, but if the incoming HttpRequest object has a
#      urlconf attribute (set by middleware), its value will be used in place of the ROOT_URLCONF setting.
#   2. Django loads that Python module and looks for the variable urlpatterns.
#      This should be a Python list of django.urls.path() and/or django.urls.re_path() instances.
#   3. Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL.
#   4. Once one of the URL patterns matches, Django imports and calls the given view, which is a simple Python function
#      The view gets passed the following arguments:
#          An instance of HttpRequest.
#          If the matched URL pattern returned no named groups, then the matches from the regular expression are provided as positional arguments.
#          The keyword arguments are made up of any named parts matched by the path expression,
#            overridden by any arguments specified in the optional kwargs argument to django.urls.path() or django.urls.re_path().
#   5. If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view. See Error handling below.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel/', include('travellog.urls')), # The include() function allows referencing other URLconfs. The idea behind include() is to make it easy to plug-and-play URLs
]
# Same Examples:
# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     path('articles/<int:year>/', views.year_archive),
#     path('articles/<int:year>/<int:month>/', views.month_archive),
#     path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
# ]
#
#       /articles/2005/03/      call funtion    views.month_archive(request, year=2005, month=3)
#       /articles/2003/         call funtion    views.special_case_2003(request)
#       /articles/2003          nothing
#       /articles/2003/03/XX/   call funtion    views.article_detail(request, year=2003, month=3, slug="XX").

# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
#       route: is a string that contains a URL pattern, Patterns don’t search GET and POST parameters, or the domain name.
#       view:  When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.

# more: https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Path converters
# Registering custom path converters
# Using regular expressions
# Including other URLconfs
