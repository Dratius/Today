from dataclasses import dataclass
from typing import Dict, Union


@dataclass
class Show:
    memory: Dict[str, Union[str, int]]

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

    def update_info(self, info: Dict):
        self.Description = info["summary"]
        self.Status = info["status"] == "Running"
        self.Schedule = info["schedule"]
        self.Maze_ID = info["id"]
        self.Maze_name = info["name"]

    def __str__(self):
        return self.Title

    def __repr__(self):
        return self.Description
