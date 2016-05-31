# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from gt.qmdocument.testing import GT_QMDOCUMENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that gt.qmdocument is properly installed."""

    layer = GT_QMDOCUMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gt.qmdocument is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'gt.qmdocument'))

    def test_browserlayer(self):
        """Test that IGtQmdocumentLayer is registered."""
        from gt.qmdocument.interfaces import (
            IGtQmdocumentLayer)
        from plone.browserlayer import utils
        self.assertIn(IGtQmdocumentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GT_QMDOCUMENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['gt.qmdocument'])

    def test_product_uninstalled(self):
        """Test if gt.qmdocument is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'gt.qmdocument'))

    def test_browserlayer_removed(self):
        """Test that IGtQmdocumentLayer is removed."""
        from gt.qmdocument.interfaces import IGtQmdocumentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IGtQmdocumentLayer, utils.registered_layers())
