import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from plugincheck.plugins.models import PluginRelease


class ViewsTestCase(TestCase):
    def test_plugin_list_json(self):
        """Verify the plugins_list JSON endpoint."""
        # NOTE: This test depends on the data in the 0002 migration.
        url = reverse('plugins_list_json')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        assert 'mime_types' in data
        assert 'plugins' in data

        flash_win_latest = PluginRelease.objects.filter(
            plugin__slug='adobe-flash-player', os='win', status='latest')
        self.assertEqual(
            flash_win_latest.count(),
            len(data['plugins']['adobe-flash-player']['versions']['win']['latest']))

        java_all_vulnerable = PluginRelease.objects.filter(
            plugin__slug='java-runtime-environment', os='all', status='vulnerable')
        self.assertEqual(
            java_all_vulnerable.count(),
            len(data['plugins']['java-runtime-environment']['versions']['all']['vulnerable']))
