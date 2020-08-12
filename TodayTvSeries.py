import requests
from typing import Dict
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

from TvShow import Show
from Website import Webs
from DataManager import Storage


class TodayTv(Webs):

    def search(self, payload: Dict) -> bool:
        adapter = HTTPAdapter(max_retries=self.max_retries)
        session = requests.Session()
        session.mount(self.TodayTvSeries, adapter)
        try:
            self.search_result = session.get(
                self.TodayTvSeries + self.search_series, params=payload,
                timeout=5)

            self.search_result.raise_for_status()

        except requests.exceptions.HTTPError as exc:
            self.error = (exc, self.search_result.status_code)
            return self.search_result.ok
        except requests.exceptions.ReadTimeout as exc:
            self.error = (exc, 1)
            return False
        except requests.exceptions.ConnectionError as exc:
            self.error = (exc, 0)
            return False

        return self.search_result.ok

    def __init__(self, show: str, search_limit: int = 30):
        super().__init__()
        self.payload = {"searchword": show, "searchphrase": "all",
                        "limit": search_limit}
        self.search_series = "search-series"
        self.search_result = ""
        self.max_retries = 5
        self.soup = BeautifulSoup
        self.error = ()
        self.connected = self.search(self.payload)
        self.__title_tags = '.uk-article-titletag a'
        self.__title_tag = "title"
        self.get_info()

    def get_info(self):
        store = Storage()
        if self.connected:
            self.soup = BeautifulSoup(self.search_result.text, "html.parser")
            t_tags_list = self.soup.select(self.__title_tags)

            for tag in t_tags_list:
                title = tag.get(self.__title_tag)
                link = self.TodayTvSeries + tag.get("href")

                store.add_show(title, link)
