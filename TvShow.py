from dataclasses import dataclass
from typing import Dict


@dataclass
class Show:
    def __init__(self, title: str, link: str):
        self.Title = title
        self.Link = link
        self.Description = ""
        self.Status = None
        self.Schedule = None
        self.Maze_ID = None
        self.Maze_name = ""
        self.Extras = {}
        self.Season = [self.Extras]
        self.Episode = {}

    def update_info(self, info: Dict):
        self.Description = info["summary"]
        self.Status = info["status"] == "Running"
        self.Schedule = info["schedule"]
        self.Maze_ID = info["id"]
        self.Maze_name = info["name"]

    def __str__(self):
        return self.Title
