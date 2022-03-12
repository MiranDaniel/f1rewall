import time

import pandas as pd



class Join:
    def __init__(self):
        self.time = time.time()


class Analytics:
    def __init__(self):
        self.joins = [

        ]

    def new_join(self):
        self.joins.append(
            Join()
        )
