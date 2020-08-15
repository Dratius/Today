from abc import ABCMeta, abstractmethod
from typing import Dict
import requests
from requests.adapters import HTTPAdapter
from requests.models import Response


class Webs(metaclass=ABCMeta):

    def __init__(self):
        self.__html = Response()
        self.max_retries = 5
        self.TodayTvSeries = "http://www.todaytvseries2.com/"
        self.TvMaze = "http://api.tvmaze.com/"
        self.IndexOf1 = "http://dl.new1music.ir/Serial/"
        self.IndexOf2 = "http://dl4.tvto.ga/Series/"
        self.IndexOfTvSeries = "https://indexoftvseries.com/"
        self._session = requests.Session()
        self._adapter = HTTPAdapter(max_retries=self.max_retries)

    def search(self, link: str, payload: Dict, timeout: int = 5) -> Response:
        self._session.mount(link, self._adapter)
        response, severe = self.html_response(link, timeout, payload)

        if not severe:
            return response
        else:
            # TODO:Handle Errors
            pass

    def html_response(self, link: str, timeout: int, payload: Dict = None):
        self.__html = self._session.get(link, params=payload, timeout=timeout)
        try:
            self.__html.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            return exc, self.__html.status_code
        except requests.exceptions.ReadTimeout as exc:
            return exc, 1
        except requests.exceptions.ConnectionError as exc:
            return exc, 2

        return self.__html, 0

    @abstractmethod
    def get_info(self, html):
        ...
