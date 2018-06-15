from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

import yafowil.plone


class IYafowilLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=yafowil.plone)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'yafowil.plone:default')


YAFOWIL_PLONE_FIXTURE = IYafowilLayer()


YAFOWIL_PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(YAFOWIL_PLONE_FIXTURE,),
    name='IYafowilLayer:IntegrationTesting'
)


YAFOWIL_PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(YAFOWIL_PLONE_FIXTURE,),
    name='IYafowilLayer:FunctionalTesting'
)