from plone.memoize.instance import memoize

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

class DoormatView(BrowserView):
    """
    """

    def getDoormatTitle(self):
        """
        """
        title = ''
        if self.context.getShowTitle():
            title = self.context.Title()
        return title
         
    def getDoormatData(self):
        """ Return a dictionary like this:
        data = [
            {   'column_title: 'Column One',
                'column_sections: [
                {   'section_title': 'De Oosterpoort',
                    'section_links': [
                        {   'link_title': 'Adres OP',
                            'link_url': 'link.naar.adres',
                            },
                        ]
                    },
                ]
            },
        ]
        """
        doormat = self.context
        data = []
        # Fetch Columns
        for column_brain in doormat.getFolderContents():
            column_dict = {
                'column_title': column_brain.Title,
                'show_title': column_brain.getShowTitle,
                }
            column_sections = []
            section_brains = column_brain.getObject().getFolderContents()

            # Fetch Categories from Column
            for section_brain in section_brains:
                section_dict = {
                    'section_title': section_brain.Title,
                    'show_title': section_brain.getShowTitle,
                    }
                section_links = []
                link_brains = section_brain.getObject().getFolderContents()

                # Loop over all link object in category
                for link_brain in link_brains:
                    # Use the link item's title, not that of the linked content
                    title = link_brain.Title
                    item = link_brain.getObject()
                    item_type = item.meta_type
                    if item_type == 'DoormatReference':
                        linked_item = item.getInternal_link()
                        if not linked_item:
                            continue
                        url = linked_item.absolute_url()
                    else:
                        # Link is an Archetypes link
                        url = link_brain.getRemoteUrl
                        if not url:
                            continue
                    link_dict = {'link_url': url, 'link_title': title}
                    section_links.append(link_dict)
                section_dict['section_links'] = section_links
                column_sections.append(section_dict)
            column_dict['column_sections'] = column_sections
            data.append(column_dict)
        return data



##code-section module-footer #fill in your manual code here
##/code-section module-footer

