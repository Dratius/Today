from Webs.Series import Scraper
from Database.DataManager import Storage
from Webs.TvShow import Show


class TvMaze(Scraper):
    def get_data(self, tv_show: Show):
        pass

    def __init__(self, title: str, link: str):
        super().__init__()
        self.payload = {"q": title}
        self.store = Storage.get_instance()
        self.__title = title
        self.__link = link
        self.__ShowSearch = "search/shows"
        self.__SingleSearch = "singlesearch/shows"
        self.__EmbedEpisodes = {"embed": "episodes"}
        self.__Lookup = "lookup/shows"
        self.__Shows = "shows/"
        html = self.search(self.TvMaze + self.__SingleSearch, self.payload)
        self.get_info(html)

    def get_info(self, html):
        if html.ok:
            book = html.json()
            if len(book) > 0:
                tv_show = self.store.get_show(self.__title, self.__link)
                tv_show.update_info(book)
