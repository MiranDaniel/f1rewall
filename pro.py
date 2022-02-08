import pickle
import sqlite3
import os

_path = "./data/dat.p"


class Pro:
    def __init__(self, enabled):
        self.enabled = enabled
        if self.enabled == False:
            return
        self.new = os.path.exists(_path)
        if self.new == False:
            self.joins = []
            self.visits = []
            self._create()
        else:
            data = pickle.load(open(_path, "rb"))

            self.joins = data["joins"]
            self.visits = data["visits"]

    def _create(self):
        pickle.dump({
            "joins": self.joins,
            "visits": self.visits
        }, open(_path, "wb+"))

    def visit(self):
        self.visits.append(0)
