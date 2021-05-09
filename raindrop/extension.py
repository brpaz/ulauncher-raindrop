import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from raindrop.preferences import PreferencesEventListener, PreferencesUpdateEventListener
from raindropio import Raindrop
from raindrop.query_listener import KeywordQueryEventListener

logger = logging.getLogger(__name__)


class RaindropExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(RaindropExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())

    def get_keyword_id(self, keyword):
        for key, value in self.preferences.items():
            if value == keyword:
                return key

        return ""

    def show_open_app_menu(self):
        """ Shows the menu to Open Raindrop website """
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name='Open Raindrop Website',
                on_enter=OpenUrlAction('https://app.raindrop.io'))
        ])

    def search(self, query):
        drops = Raindrop.search(self.rd_client, word=query, perpage=10)

        if len(drops) == 0:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='No results found matcing your criteria',
                    highlightable=False)
            ])

        items = []
        for drop in drops:
            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name=drop.title,
                                    description=drop.excerpt,
                                    on_enter=OpenUrlAction(drop.link)))
        return RenderResultListAction(items)
