from TodayTvSeries import TodayTv
import requests


class Search:

    def __init__(self, query: str, limit: int = 30):
        self.TodayTvSeries = "http://www.todaytvseries2.com/"
        self.TvMaze = "http://api.tvmaze.com/"
        self.html = None
        self.query = query
        self.limit = limit
        self.error = None

    def browse_tv(self):
        try:
            self.html = requests.get(
                f"{self.TodayTvSeries}search-series?searchword="
                f"{self.query}&searchphrase=all&limit={self.limit}").text

        except Exception as exc:
            self.error = exc
            self.connected = False

        self.connected = True

    def search_maze(self):
        ...
