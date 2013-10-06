# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.base import ATCTContent
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Doormat.config import *

from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget

schema = Schema((

    ReferenceField(
        name='collection',
        widget=ReferenceBrowserWidget(
            label='Collection',
            label_msgid='Doormat_label_collection',
            i18n_domain='Doormat',
        ),
        allowed_types="('Topic', 'Collection')",
        relationship="internally_references_to_collection",
    ),
    ReferenceField(
        name='showMoreLink',
        widget=ReferenceBrowserWidget(
            label=""""Show more" link""",
            description="Optionally, add a location for an extra link that will be displayed below the items, like a link to the collection itself.",
            label_msgid='Doormat_label_showMoreLink',
            description_msgid='Doormat_help_showMoreLink',
            i18n_domain='Doormat',
        ),
        relationship="more_link_links_to_internal",
    ),
    StringField(
        name='showMoreText',
        widget=StringField._properties['widget'](
            label=""""Show more" text""",
            description="""The text for the "Show more" link.""",
            label_msgid='Doormat_label_showMoreText',
            description_msgid='Doormat_help_showMoreText',
            i18n_domain='Doormat',
        ),
    ),
    IntegerField(
        name='limit',
        widget=IntegerField._properties['widget'](
            label="Limit number of items",
            description="Maximum number of items to be shown, leave blank for all items.",
            label_msgid='Doormat_label_limit',
            description_msgid='Doormat_help_limit',
            i18n_domain='Doormat',
        ),
    ),
    BooleanField(
        name='showTime',
        widget=BooleanField._properties['widget'](
            label="Show time",
            description="Show the item's last modification time",
            label_msgid='Doormat_label_showTime',
            description_msgid='Doormat_help_showTime',
            i18n_domain='Doormat',
        ),
    ),

),
)

DoormatCollection_schema = BaseSchema.copy() + \
    schema.copy()


class DoormatCollection(ATCTContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDoormatCollection)

    meta_type = 'DoormatCollection'
    _at_rename_after_creation = True

    schema = DoormatCollection_schema


registerType(DoormatCollection, PROJECTNAME)
