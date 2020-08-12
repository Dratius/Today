import requests
from typing import Dict
from requests.adapters import HTTPAdapter

from TvShow import Show
from Website import Webs
from DataManager import Storage


class TvMaze(Webs):

    def search(self, payload: Dict) -> bool:
        adapter = HTTPAdapter(max_retries=self.max_retries)
        session = requests.Session()
        session.mount(self.TvMaze, adapter)
        try:
            self.api_results = session.get(
                self.TvMaze + self.__SingleSearch, params=payload).json()
        except Exception as exc:
            self.error = exc
            return False

        return True

    def __init__(self, title: str, link: str):
        super().__init__()
        self.max_retries = 5
        self.api_results = {}
        self.error = None
        self.payload = {"q": title}
        self.__title = title
        self.__link = link
        self.__ShowSearch = "search/shows"
        self.__SingleSearch = "singlesearch/shows"
        self.__EmbedEpisodes = {"embed": "episodes"}
        self.__Lookup = "lookup/shows"
        self.__Shows = "shows/"
        self.connected = self.search(self.payload)
        self.get_info()

    def get_info(self):
        store = Storage.get_instance()
        if self.connected:
            if len(self.api_results) > 0:
                tv_show: Show = store.Series.get((self.__title, self.__link))
                tv_show.update_info(self.api_results)
