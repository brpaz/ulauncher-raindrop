from ulauncher.api.client.EventListener import EventListener


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    def on_event(self, event, extension):

        kw_id = extension.get_keyword_id(event.get_keyword())
        query = event.get_argument() or ""

        if kw_id == 'kw_open':
            return extension.show_open_app_menu()

        if kw_id == 'kw_unsorted':
            return extension.unsorted(query)

        return extension.search(query)
