from bs4 import BeautifulSoup

from Webs.Series import Scraper
from Database.DataManager import Storage


class TodayTv(Scraper):
    def __init__(self, show: str, search_limit: int = 30):
        super().__init__()
        self.store = Storage.get_instance()
        self.__payload = {
            "searchword": show,
            "searchphrase": "all",
            "limit": search_limit}

        self.__search_series = "search-series"
        self.__title_tags = '.uk-article-titletag a'
        self.__title_tag = "title"
        html = self.search(
            self.TodayTvSeries + self.__search_series, self.__payload
        )
            
        self.get_info(html)

    def get_info(self, html):
        soup = BeautifulSoup(html.text, "html.parser")
        t_tags_list = soup.select(self.__title_tags)

        for tag in t_tags_list:
            title = tag.get(self.__title_tag)
            link = self.TodayTvSeries + tag.get("href")

            self.store.add_show(title, link)

    def get_data(self, tv_show):
        """
        @type tv_show: Show
        """
        response = self.search(tv_show.Url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            tv_show_data = soup.select(".row2")
            row: BeautifulSoup
            for row in tv_show_data:
                curr_row_episode = row.select(".cell2")[0].getText()
                episode_quality = row.select(".cell4")[0].getText()
                episode_size = row.select(".cell3")[0].getText()
                episode_link = row.select(
                    '.cell4 .hvr-icon-sink-away')[0].get("href")

                self.store.add_tv_show_data(
                    tv_show,
                    episode=curr_row_episode,
                    quality=episode_quality,
                    size=episode_size,
                    url=episode_link,
                    episode_url=tv_show.Url
                )
            return True
