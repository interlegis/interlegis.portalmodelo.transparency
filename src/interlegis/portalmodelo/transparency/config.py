# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from zope.interface import implements

PROJECTNAME = 'interlegis.portalmodelo.transparency'


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'interlegis.portalmodelo.transparency:uninstall',
            u'interlegis.portalmodelo.transparency.upgrades.v1010:default'
        ]


class HiddenProducts(object):
    implements(qi_interfaces.INonInstallable)

    def getNonInstallableProducts(self):
        # Add in here upgrade steps
        return [
            u'interlegis.portalmodelo.transparency.upgrades.v1010'
        ]
