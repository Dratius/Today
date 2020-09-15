import re
from typing import Dict

from Webs.TvShow import Show


class Storage:
    __instance__ = None
    Series = {}
    TvShow = None

    def __init__(self):
        if Storage.__instance__ is None:
            Storage.__instance__ = self

        else:
            raise Exception("This Class can only be initialised once.")

    @staticmethod
    def get_instance():
        if Storage.__instance__ is None:
            Storage()

        return Storage.__instance__

    @staticmethod
    def add_show(title, link):
        tv_show = Show(title, link)
        Storage.Series.update({(title, link): tv_show})

    @staticmethod
    def get_show(name: str, link: str) -> Show:
        return Storage.Series.get((name, link))

    @staticmethod
    def add_extra(tv_show: Show, **new):
        tv_show.Extras.update({
            new["name"]: {
                "Name": new["name"],
                "Links": {
                    new["quality"]: {
                        "Quality": new["quality"],
                        "Link": new["link"],
                        "Size": new["size"]
                    }}}})

    @staticmethod
    def update_quality_section(quality_section: Dict, **update):
        quality_section.update({
            update["quality"]: {
                "Quality": update["quality"],
                "Link": update["link"],
                "Size": update["size"]
            }})

    @staticmethod
    def update_episode_section(episode_section: Dict, **update):
        episode_section.update({
            "link": update["url"],
            update["episode"]: {
                "Episode": update["episode"],
                "Links": {
                    update["quality"]: {
                        "Quality": update["quality"],
                        "Link": update["link"],
                        "Size": update["size"]
                    }}}})

    def add_tv_show_data(self, tv_show: Show, **data):
        title_pattern = re.compile(r"(S\d\d)(E\d\d)+")
        quality_pattern = re.compile(r"480p|720p|1080p")
        codec_pattern = re.compile(r"x264|x265|x266|HEVC")
        current_season = tv_show.memory["last season"]

        episode_ = data["episode"]
        quality_ = data["quality"]
        title_matched = title_pattern.search(episode_)
        quality_matched = quality_pattern.search(quality_)
        codec_matched = codec_pattern.search(quality_)
        extras = title_matched is None
        quality_available = quality_matched is not None

        url_ = data["url"]
        size_ = data["size"]
        episode_url_ = data["episode_url"]
        prev_episode = tv_show.memory["last episode"]
        prev_quality = tv_show.memory["prev quality matched"]

        if not extras:
            # Scanning for quality updates
            updating_quality =\
                title_matched.group() == prev_episode and quality_available
        else:
            updating_quality = episode_ == prev_episode and quality_available

        if updating_quality:
            # Implementing Quality Updates
            quality = quality_matched.group()
            if quality == prev_quality and codec_matched is not None:
                quality = quality_matched.group() + " " + codec_matched.group()
            else:
                quality = quality_matched.group()

            if extras:  # update entry's quality section.
                q_section = tv_show.Extras[episode_]["Links"]
                self.update_quality_section(
                    quality_section=q_section,
                    quality=quality,
                    link=url_,
                    size=size_
                )
            else:
                episode = title_matched.group()
                q_section = tv_show.Season[current_season][episode[3:]][
                    "Links"]
                self.update_quality_section(
                    quality_section=q_section,
                    quality=quality,
                    link=url_,
                    size=size_
                )

        if extras:
            # Saving Progress
            if updating_quality:
                save_to_memory(tv_show, episode_, quality_matched.group())
                return
            save_to_memory(tv_show, episode_, quality_)

        else:
            save_to_memory(tv_show,
                           title_matched.group(),
                           quality_matched.group())
            if updating_quality:
                return

        # New Episode / Extra
        if extras:  # add new extra.
            if quality_matched is None:
                self.add_extra(
                    tv_show,
                    name=episode_,
                    link=url_,
                    size=size_,
                    quality="480p"
                )
            else:
                self.add_extra(
                    tv_show,
                    name=episode_,
                    link=url_,
                    size=size_,
                    quality=quality_matched.group()
                )
        else:
            current_season = capacity = \
                int(title_matched.group(1)[1:])
            tv_show.memory["last season"] = current_season

            if len(tv_show.Season) - 1 < capacity:
                tv_show.Season.extend(dict() for i in range(capacity))

            episodes = tv_show.Season[current_season]
            episode = title_matched.group()[3:]

            if quality_matched is None:
                self.update_episode_section(
                    url=episode_url_,
                    episode_section=episodes,
                    episode=episode,
                    quality="480p",
                    link=url_,
                    size=size_
                )
            else:
                self.update_episode_section(
                    url=episode_url_,
                    episode_section=episodes,
                    episode=episode,
                    quality=quality_matched.group(),
                    link=url_,
                    size=size_
                )


def save_to_memory(tv_show: Show, episode, quality):
    tv_show.memory["last episode"] = episode
    tv_show.memory["prev quality matched"] = quality
