import time

from source import discord
import threading


class InvitePool:
    def __init__(self):
        self.pool = [

        ]
        self.poolSize = 3
        self.poolSizeLimit = 25

        self.poolSizeDefault = self.poolSize


    def debug(self):
        #return  # disable debug mode

        print(self.pool)

    def add(self):
        self.debug()
        print("Creating new invite")
        self.pool.append(
            (
                discord.invite(),
                time.time()
            )
        )

    def check(self):
        self.debug()
        print("Checking invite pool")
        for i in self.pool:
            if time.time() + 300 < time.time() + 30:  # 300 = max invite time, 30 = room for user to join
                self.pool.remove(i)

        if len(self.pool) < self.poolSize:
            threading.Thread(target=self.fill).start()
        if len(self.pool) == 0:
            self.poolSize += 1 if self.poolSize < self.poolSizeLimit+1 else 0
            print(f"Inflating invite pool to {self.poolSize}")
        else:
            self.poolSize = self.poolSize - 1 if self.poolSize > self.poolSizeDefault else self.poolSizeDefault
            print(f"Deflating invite pool to {self.poolSize}")

    def fill(self):
        self.debug()
        print("Filling")
        for i in range(self.poolSize - len(self.pool)):
            if len(self.pool) < self.poolSize:
                self.add()
            else:
                break

    def get(self):
        self.debug()
        print("Returning new invite")
        threading.Thread(target=self.check).start()
        threading.Thread(target=self.fill).start()
        if len(self.pool) > 0:
            val = self.pool[0]
            self.pool.remove(val)
            return val[0]
        else:
            time.sleep(10/3)
            return self.get()
