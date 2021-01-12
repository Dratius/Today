from requests.adapters import HTTPAdapter
from abc import ABCMeta, abstractmethod
from requests.models import Response
from typing import Dict
import requests

from Webs.TvShow import Show


class Scraper(metaclass=ABCMeta):

    def __init__(self):
        self.__html = Response()
        self.max_retries = 5
        self.TodayTvSeries = "http://www.todaytvseries2.com/"
        self.TvMaze = "http://api.tvmaze.com/"
        self.IndexOf1 = "http://dl.new1music.ir/Serial/"
        self.IndexOfTvTo = "http://dl4.tvto.ga/Series/"
        self.IndexOfTvSeries = "https://indexoftvseries.com/"
        self._session = requests.Session()
        self._adapter = HTTPAdapter(max_retries=self.max_retries)

    def search(self, link, payload: Dict = None, timeout: int = 5) -> Response:
        self._session.mount(link, self._adapter)
        response, severe = self.html_response(link, payload, timeout)

        if not severe:
            return response
        else:
            title, message = self.handle_error(response, severe)
            raise TvExceptions.TvException(title, message)

    def html_response(self, link: str, payload: Dict, timeout: int):
        try:
            self.__html = self._session.get(
                link, params=payload, timeout=timeout)
        except requests.exceptions.Timeout as exc:
            return exc, 1
        except requests.exceptions.ConnectionError as exc:
            return exc, 2

        return self.__html, 0

    @abstractmethod
    def get_info(self, html: Response):
        ...

    @abstractmethod
    def get_data(self, tv_show: Show):
        ...
