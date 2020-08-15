
from Website import Webs
from DataManager import Storage


class TvMaze(Webs):
    def __init__(self, title: str, link: str):
        super().__init__()
        self.payload = {"q": title}
        self.__title = title
        self.__link = link
        self.__ShowSearch = "search/shows"
        self.__SingleSearch = "singlesearch/shows"
        self.__EmbedEpisodes = {"embed": "episodes"}
        self.__Lookup = "lookup/shows"
        self.__Shows = "shows/"
        html = self.search(self.TvMaze, self.payload)
        self.get_info(html)

    def get_info(self, html):
        store = Storage.get_instance()
        if len(html.json()) > 0:
            tv_show = store.get_show(self.__title, self.__link)
            tv_show.update_info(html.json())
