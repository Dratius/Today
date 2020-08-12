from typing import Any, Dict, List
from TvShow import Show


class Storage:
    __instance__ = None
    Series = {}

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
