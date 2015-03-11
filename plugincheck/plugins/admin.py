from django.contrib import admin

from plugincheck.base.admin import admin_site
from plugincheck.plugins.models import Mime, Plugin, PluginAlias, PluginRelease


@admin.register(Mime, site=admin_site)
class MimeAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Plugin, site=admin_site)
class PluginAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name')

    filter_horizontal = ('mimes',)


@admin.register(PluginAlias, site=admin_site)
class PluginAliasAdmin(admin.ModelAdmin):
    list_display = (
        'plugin',
        'alias',
        'is_regex')

    list_filter = (
        'plugin',
        'is_regex')


@admin.register(PluginRelease, site=admin_site)
class PluginReleaseAdmin(admin.ModelAdmin):
    list_display = (
        'plugin',
        'os',
        'version',
        'status')

    list_filter = (
        'plugin',
        'os',
        'status')
