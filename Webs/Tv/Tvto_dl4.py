import re
import bs4
from bs4 import BeautifulSoup

from Webs.Series import Scraper
from Database.DataManager import Storage
from Webs.TvShow import Show


class IndexOf(Scraper):

    store: Storage

    def __init__(self, query):
        super().__init__()
        self.__title_tag = "a"
        self.store = Storage.get_instance()
        index_html = self.search(self.IndexOfTvTo)
        self.query_searcher = re.compile(query)
        self.get_info(index_html)

    def get_info(self, html):
        soup = BeautifulSoup(html.text, "html.parser")
        t_tags_list = soup.select(self.__title_tag)

        tag: bs4.element.Tag
        for tag in t_tags_list:
            title = tag.getText().rstrip("/")
            link = self.IndexOfTvTo + tag.get("href")
            title_matched = self.query_searcher.search(title)

            if title_matched is not None:
                self.store.add_show(title, link)

    def get_data(self, tv_show: Show, url=None):

        if url is None:
            response = self.search(tv_show.Url)
        else:
            response = self.search(url)

        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            t_tags_list = soup.select(self.__title_tag)
            t_tags_list.pop(0)

            tag: bs4.element.Tag
            for tag in t_tags_list:
                title = tag.getText()
                if url is None:
                    link = tv_show.Url + tag.get("href")
                else:
                    link = url + tag.get("href")

                if title.endswith("/"):
                    self.get_data(tv_show, link)
                else:
                    size = str(int(tag.next_sibling[-11:-2]) / 1024 ** 2)
                    self.store.add_tv_show_data(
                        tv_show,
                        episode=title,
                        quality=title,
                        size=size,
                        url=link,
                        episode_url=link
                    )


