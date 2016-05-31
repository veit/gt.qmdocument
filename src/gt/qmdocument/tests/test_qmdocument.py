# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from gt.qmdocument.testing import GT_QMDOCUMENT_INTEGRATION_TESTING  # noqa
from gt.qmdocument.interfaces import IQMDocument

import unittest2 as unittest


class QMDocumentIntegrationTest(unittest.TestCase):

    layer = GT_QMDOCUMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='QMDocument')
        schema = fti.lookupSchema()
        self.assertEqual(IQMDocument, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='QMDocument')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='QMDocument')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IQMDocument.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('QMDocument', 'QMDocument')
        self.assertTrue(
            IQMDocument.providedBy(self.portal['QMDocument'])
        )
