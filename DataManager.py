from typing import Any, Dict, List
from TvShow import Show


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
    def add_season(tv_show: Show, **new):
        tv_show.Season.append({
            new["episode"]: {
                "Episode": new["episode"],
                "Links": {new["quality"]: {
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
            update["episode"]: {
                "Episode": update["episode"],
                "Links": {
                    update["quality"]: {
                        "Quality": update["quality"],
                        "Link": update["link"],
                        "Size": update["size"]
                    }}}})
