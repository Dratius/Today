import re
from bs4 import BeautifulSoup

from Webs.Series import Scraper
from Webs.Tv.DataManager import Storage


class TodayTv(Scraper):
    def __init__(self, show: str, search_limit: int = 30):
        super().__init__()
        self.store = Storage()
        self.__payload = {
            "searchword": show,
            "searchphrase": "all",
            "limit": search_limit}

        self.__search_series = "search-series"
        self.__title_tags = '.uk-article-titletag a'
        self.__title_tag = "title"
        self.html = self.search(
            self.TodayTvSeries + self.__search_series, self.__payload
        )
        self.get_info(self.html)

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
        self._session.mount(self.TodayTvSeries, self._adapter)
        response = self.search(tv_show.Link)

        title_pattern = re.compile(r"(S\d\d)(E\d\d)+")
        quality_pattern = re.compile(r"480p|720p|1080p")
        current_season = 0
        prev_row_episode = ""

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
                title_matched = title_pattern.search(curr_row_episode)
                quality_matched = quality_pattern.search(episode_quality)
                extras = title_matched is None

                if curr_row_episode == prev_row_episode:
                    if extras:  # update entry's quality section.
                        quality = tv_show.Extras[curr_row_episode]["Links"]
                        self.store.update_quality_section(
                            quality_section=quality,
                            quality=episode_quality,
                            link=episode_link,
                            size=episode_size
                        )
                        continue
                    else:
                        quality = tv_show.Season[current_season][
                            curr_row_episode[3:]]["Links"]
                        self.store.update_quality_section(
                            quality_section=quality,
                            quality=episode_quality,
                            link=episode_link,
                            size=episode_size
                        )
                        continue
                else:
                    prev_row_episode = curr_row_episode

                if extras:  # add new extra.
                    if quality_matched is None:
                        self.store.add_extra(tv_show,
                                             name=curr_row_episode,
                                             link=episode_link,
                                             size=episode_size,
                                             quality="480p"
                                             )
                    else:
                        self.store.add_extra(tv_show,
                                             name=curr_row_episode,
                                             link=episode_link,
                                             size=episode_size,
                                             quality=episode_quality
                                             )
                else:
                    current_season = capacity = int(title_matched.group(1)[1:])

                    if len(tv_show.Season) - 1 < capacity:
                        tv_show.Season.extend(dict() for i in range(capacity))

                    episodes = tv_show.Season[current_season]

                    if quality_matched is None:
                        self.store.update_episode_section(
                            episode_section=episodes,
                            episode=curr_row_episode[3:],
                            quality="480p",
                            link=episode_link,
                            size=episode_size
                        )
                    else:
                        self.store.update_episode_section(
                            episode_section=episodes,
                            episode=curr_row_episode[3:],
                            quality=episode_quality,
                            link=episode_link,
                            size=episode_size
                        )
