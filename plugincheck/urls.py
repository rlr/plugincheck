from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from plugincheck.base.admin import admin_site


# Autodiscover admin.py files in your project.
admin.autodiscover()


# copy_registry copies ModelAdmins registered with the default site, like
# the built-in Django User model.
admin_site.copy_registry(admin.site)


urlpatterns = patterns('',
    url('^$', RedirectView.as_view(url='/admin/'), name='home'),

    url(r'', include('django_browserid.urls')),
    url(r'', include('plugincheck.plugins.urls')),

    url(r'^admin/', include(admin_site.urls)),
)
