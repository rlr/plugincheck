from django.db import models


class Mime(models.Model):
    """Represents a MIME type."""
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Plugin(models.Model):
    """Represents a browser plugin."""
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default=u'')
    vendor = models.CharField(max_length=255, blank=True, default=u'')
    url = models.URLField(max_length=255, blank=True, default=u'')
    mimes = models.ManyToManyField(Mime, blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'[{slug}] {name}'.format(
            slug=self.slug,
            name=self.name)


class PluginAlias(models.Model):
    """Represents an alias for a plugin."""
    plugin = models.ForeignKey(Plugin)
    alias = models.CharField(max_length=255)
    is_regex = models.BooleanField(default=False)

    class Meta(object):
        unique_together = (
            'plugin',
            'alias',
            'is_regex')

    def __unicode__(self):
        return '[{plugin}] {alias}'.format(
            plugin=self.plugin.slug,
            alias=self.alias)


class PluginRelease(models.Model):
    """Represents a plugin release."""
    # Statuses
    UNKNOWN = u'unknown'
    LATEST = u'latest'
    OUTDATED = u'outdated'
    VULNERABLE = u'vulnerable'
    SHOULD_DISABLE = u'should_disable'
    STATUS_CHOICES = (
        (UNKNOWN, UNKNOWN),
        (LATEST, LATEST),
        (OUTDATED, OUTDATED),
        (VULNERABLE, VULNERABLE),
        (SHOULD_DISABLE, SHOULD_DISABLE),
    )

    # OSes
    ALL = u'all'
    WINDOWS = u'win'
    MAC = u'mac'
    LINUX = u'lin'
    OS_CHOICES = (
        (ALL, u'All'),
        (WINDOWS, u'Windows'),
        (MAC, u'Mac OS X'),
        (LINUX, u'Linux'),
    )

    plugin = models.ForeignKey(Plugin)
    os = models.CharField(max_length=32, choices=OS_CHOICES, default=ALL)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=UNKNOWN)
    name = models.CharField(max_length=255, blank=True, default=u'')
    description = models.TextField(blank=True, default=u'')
    vendor = models.CharField(max_length=255, blank=True, default=u'')
    url = models.URLField(max_length=255, blank=True, default=u'')
    vulnerability_description = models.TextField(blank=True, default=u'')
    vulnerability_url = models.URLField(max_length=255, blank=True, default=u'')
    filename = models.CharField(max_length=255, blank=True, default=u'')
    version = models.CharField(max_length=255, blank=True, default=u'')
    detected_version = models.CharField(max_length=255, blank=True, default=u'')
    detection_type = models.CharField(max_length=255, blank=True, default=u'*')
    xpi_location = models.CharField(max_length=255, blank=True, default=u'')
    manual_installation_url = models.URLField(max_length=255, blank=True, default=u'')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        unique_together = (
            'plugin',
            'os',
            'version',
            'detected_version',
            'detection_type')

    def __unicode__(self):
        return '[{plugin}][{os}] {version}'.format(
            plugin=self.plugin.slug,
            os=self.os,
            version=self.version)
