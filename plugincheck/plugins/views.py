from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control

from plugincheck.base.decorators import cors_enabled
from plugincheck.plugins.models import Mime, Plugin, PluginRelease


@cors_enabled('*')
@cache_control(max_age=3600)
def plugins_list_json(self):
    """Returns the list of plugins in json.

    The JSON returned looks like this:
        {
            "mime_types": ["application/pdf", ...],
            "plugins": {
                "adobe-flash-player": {
                    "display_name": "Adobe Flash Player",
                    "description": "",
                    "url": ""http://www.adobe.com/go/getflashplayer",
                    "mimes": ["application/x-shockwave-flash",...],
                    "regex": [".*Flash.*", ...],
                    "versions": {
                        "win": {
                            "latest": [{
                                "status": "latest",
                                "os_name": "win",
                                "vulnerability_description": "",
                                "vulnerability_url": "",
                                "detection_type": "*",
                                "version": "16.0.0.305",
                                "detected_version": "16.0.0.305"}, ...],
                            "vulnerable":[...]
                        }, ...
                    }
                }, ...
            }
        }
    """
    # This view grabs all the data needed from the DB, massages it and
    # shapes it for consumption by the current frontend.

    data = {}

    # Plugins:
    plugins = {}
    for p in Plugin.objects.all():
        mimes = p.mimes.all().values_list('name', flat=True)
        regex = p.pluginalias_set.filter(is_regex=True).values_list('alias', flat=True)
        plugin = {
            'display_name': p.name,
            'description': p.description,
            'url': p.url,
            'mimes': list(mimes),
            'regex': list(regex),
            'versions': {},
        }
        plugins[p.slug] = plugin

    data['plugins'] = plugins

    # Plugin releases:

    # We only care about releases with status = latest, vulnerable.
    statuses_we_care_about = [PluginRelease.LATEST, PluginRelease.VULNERABLE]

    # We only care about the current set of OSes we support. There is legacy
    # data that we don't want to show.
    oses_we_care_about = [os[0] for os in PluginRelease.OS_CHOICES]

    # The releases we care about are for the OSes and statuses we care about.
    releases_we_care_about = PluginRelease.objects.filter(
        status__in=statuses_we_care_about,
        os__in=oses_we_care_about)

    for pr in releases_we_care_about.select_related('plugin'):
        release = {
            'status': pr.status,
            'vulnerability_description': pr.vulnerability_description,
            'vulnerability_url': pr.vulnerability_url,
            'version': pr.version,
            'detected_version': pr.detected_version,
            'detection_type': pr.detection_type,
            'os_name': pr.os,
        }
        (plugins[pr.plugin.slug]['versions']
            .setdefault(pr.os, {})
            .setdefault(pr.status, [])
            .append(release))

    # MIME types:
    mime_types = Mime.objects.all().values_list('name', flat=True)
    data['mime_types'] = list(mime_types)

    return JsonResponse(data)
