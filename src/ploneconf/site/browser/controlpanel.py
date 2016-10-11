# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IPloneconfControlPanel(Interface):

    date_of_conference = schema.Date(
        title=u'First day of the conference',
        required=False,
        default=date(2016, 10, 17),
    )

    talk_submission_open = schema.Bool(
        title=u'Allow talk submission',
        description=u'Allow the submission of talks for anonymous user',
        default=False,
        required=False,
    )


class PloneconfControlPanelForm(RegistryEditForm):
    schema = IPloneconfControlPanel
    schema_prefix = "ploneconf"
    label = u'Ploneconf Settings'


PloneconfControlPanelView = layout.wrap_form(
    PloneconfControlPanelForm, ControlPanelFormWrapper)
