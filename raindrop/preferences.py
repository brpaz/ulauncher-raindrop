""" Extension preferences Listeners """

from ulauncher.api.client.EventListener import EventListener
from raindropio import API


class PreferencesEventListener(EventListener):
    """ Handles preferences initialization event """
    def on_event(self, event, extension):
        """ Handle event """
        extension.rd_client = API(event.preferences["access_token"])


class PreferencesUpdateEventListener(EventListener):
    """ Handles Preferences Update event """
    def on_event(self, event, extension):
        if event.id == 'access_token':
            extension.rd_client = API(event.new_value)
