from abc import ABCMeta, abstractmethod
from typing import Dict


class Webs(metaclass=ABCMeta):

    def __init__(self):
        self.TodayTvSeries = "http://www.todaytvseries2.com/"
        self.TvMaze = "http://api.tvmaze.com/"
        self.IndexOf1 = "http://dl.new1music.ir/Serial/"
        self.IndexOf2 = "http://dl4.tvto.ga/Series/"
        self.IndexOfTvSeries = "https://indexoftvseries.com/"

    @abstractmethod
    def search(self, payload: Dict): ...

    @abstractmethod
    def get_info(self): ...
