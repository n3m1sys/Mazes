from numpy import empty
import maze as mz
import random
import time
import os


DELAY=0.5

search_pattern = {
    # coming : [where to search]
    "left" : ["up","down","right"],
    "up"   : ["left","down","right"],
    "down" : ["left","up","right"],
    "right": ["left","up","down"]
}

operations = {
    "left" : {
        "move" : "move_left",
        "check": "can_move_left"
    },
    "up" : {
        "move" : "move_up",
        "check": "can_move_up"
    },
    "down" : {
        "move" : "move_down",
        "check": "can_move_down"
    },
    "right": {
        "move" : "move_right",
        "check": "can_move_right"
    }
}

go_back = {
    "left" : "right",
    "up"   : "down",
    "down" : "up",
    "right": "left"
}

class DFS:

    def __init__(self):
        """ Constructor method
        """
        self.m = mz.Maze()
        self.m.recdiv_generation_start()
        self.path = []

    def possible_paths(self, coming="up"):
        """ Searches for possible paths in the maze

        Args:
            coming (str, optional): Where was the player coming from. Defaults to "up".

        Returns:
            List[str]: List with the directions that the player's able to go
        """
        paths = []
        for direction in search_pattern[coming]:
            res = getattr(self.m,operations[direction]["check"])()
            if res:
                paths.append(direction)
        return paths
    
    def walk(self, direction):
        """ Walks into a path

        Args:
            direction (str): Direction of the path
        """
        time.sleep(DELAY)
        self.path.append(direction)
        getattr(self.m,operations[direction]["move"])()
        if self.m.has_ended():
            return
        paths = self.possible_paths(coming=go_back[direction])
        if paths is empty:
            self.back(direction)
            return
        os.system("clear")
        print("Walk " + direction)
        print(self.path)
        print(self.m)
        random.shuffle(paths)
        for path in paths:
            self.walk(path)
            if self.m.has_ended():
                return
        self.back(direction)
        
    def back(self, coming):
        """ Goes back from the path the player was going

        Args:
            coming (str): Direction the player was coming
        """
        time.sleep(DELAY)
        getattr(self.m,operations[go_back[coming]]["move"])()
        self.path = self.path[:-1]
        os.system("clear")
        print("Go back " + go_back[coming])
        print(self.path)
        print(self.m)

    def start(self):
        """ Starts the algorithm
        """
        if self.m.has_ended():
            return
        paths = self.possible_paths()
        if paths is empty:
            print("Impossible Maze")
            return
        print(self.path)
        print(self.m)
        random.shuffle(paths)
        for path in paths:
            self.walk(path)
            if self.m.has_ended():
                os.system("clear")
                print(str(self.path))
                print(str(self.m))
                print("Maze completed")
                return
        print("Impossible Maze")
