# -*- coding: utf-8 -*-

from interlegis.portalmodelo.transparency.interfaces import ICSVData
from interlegis.portalmodelo.transparency.testing import INTEGRATION_TESTING
from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID
from zope.component import createObject
from zope.component import queryUtility

import unittest2 as unittest


class ContentTypeTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('CSVData', 'example')
        self.example = self.folder['example']

    def test_adding(self):
        self.assertTrue(ICSVData.providedBy(self.example))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='CSVData')
        self.assertIsNotNone(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='CSVData')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(ICSVData.providedBy(new_object))

    def test_is_referenceable(self):
        self.assertTrue(IReferenceable.providedBy(self.example))
        self.assertTrue(IAttributeUUID.providedBy(self.example))
