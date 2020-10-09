from Webs.Tv import TodayTvSeries
from Webs.Tv import TvMaze
from Webs.Tv import Tvto_dl4
from Webs.TvShow import Show


class Search:
    def __init__(self, query):
        self.search = query
        self.results = {}

    def start(self):
        self.results = self.search_today_tv()
        if len(self.results) > 0:
            self.add_maze_data(self.results)
            return True

        self.results = self.search_tv_to()
        if len(self.results) > 0:
            self.add_maze_data(self.results)
            return True

        return False

    def search_today_tv(self):
        site = TodayTvSeries.TodayTv(self.search)
        return site.store.Series

    def search_tv_to(self):
        site = Tvto_dl4.IndexOf(self.search)
        return site.store.Series

    @staticmethod
    def add_maze_data(results):
        show: Show
        for show in results:
            TvMaze.TvMaze(show.Title, show.Url)
