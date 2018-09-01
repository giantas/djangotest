"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy
from .views import home

admin.site.site_header = ugettext_lazy('Feedback Admin')    # Text to put in each page's <h1> (and above login form).
admin.site.site_title = ugettext_lazy('Feedback')   # Text to put at the end of each page's <title>.
admin.site.index_title = ugettext_lazy('Feedback Administration')   # Text to put at the top of the admin index page.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^feedback/', include('fback.urls')),
    url(r'^$', home, name='home_page'),
]
