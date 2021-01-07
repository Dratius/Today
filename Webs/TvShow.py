from dataclasses import dataclass


@dataclass
class Show:
    def __init__(self, title: str, link: str):
        self.Title = title
        self.Url = link
        self.Description = ""
        self.Status = None
        self.Schedule = None
        self.Maze_ID = None
        self.Maze_name = ""
        self.Extras = {}
        self.Season = [self.Extras]
        self.memory = {"last episode": "0",
                       "last season": 0,
                       "prev quality matched": ""
                       }

    def update_info(self, info):
        self.Description = info["summary"]
        self.Status = info["status"] == "Running"
        self.Schedule = info["schedule"]
        self.Maze_ID = info["id"]
        self.Maze_name = info["name"]
