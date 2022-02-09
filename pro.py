import pickle
import sqlite3
import os
import time
from datetime import datetime
import arrow

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
        t = time.time()
        t = t - (t % 60)
        self.visits.append(t)

    def out(self):
        d = [
            {
                "data": {},
                "labels": []
            }
        ]

        t = time.time()
        t = t - (t % 60)+60

        print("Range done")

        for i in range(60):
            i = 60-i
            i = t-60*i
            d[0]["labels"].append(i)
            d[0]["data"][i] = 0
        print("Range done")

        for i in self.visits:
            if i in d[0]["labels"]:
                d[0]["data"][i] += 1

        d[0]["data"] = list(d[0]["data"].values())

        print("Enum")
        for i, j in enumerate(d[0]["labels"]):
            d[0]["labels"][i] = datetime.fromtimestamp(j).strftime("%H:%M")
        print(d)
        print("Enum")
        self._create()
        return d
