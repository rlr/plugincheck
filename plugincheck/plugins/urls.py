from django.conf.urls import patterns, url


urlpatterns = patterns(
    'plugincheck.plugins.views',

    url(r'^plugins_list.json$', 'plugins_list_json', name='plugins_list_json'),
)
