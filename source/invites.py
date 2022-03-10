import time

from source import discord
from blessed import Terminal
import threading

term = Terminal()


class InvitePool:
    def __init__(self):
        self.pool = [

        ]
        self.poolSize = 3 # amount of invites to keep in memory
        self.poolSizeLimit = 25 # max invites to be scaled to

        self.inviteSize = 1
        self.inviteSizeLimit = 3 # higher number = more invites/minute at the cost of security

        self.poolSizeDefault = self.poolSize

    def debug(self):
        return  # disable debug mode

        print("::InvitePool::DEBUG::  " + str(self.pool))

    def add(self):
        print("::InvitePool::  " + term.underline("Creating new invite"))
        x = discord.invite(
            size=self.inviteSize
        )
        if x is None:
            return

        self.pool.append(
            [
                x,
                time.time(),
                self.inviteSize
            ]
        )
        self.debug()

    def check(self):
        print("::InvitePool::  " + "Checking invite pool")
        for i in self.pool[:]:
            if i[1] + 300 < time.time() + 30:  # 300 = max invite time, 30 = room for user to join
                print("::InvitePool::  " + term.red(f"Expired invite removed {i[0]}"))
                try:
                    self.pool.remove(i)
                except ValueError:  # already removed by another thread
                    pass  # ignore, not an issue
            if i[2] < 1:
                print("::InvitePool::  " + term.red(f"Used invite removed {i[0]}"))
                try:
                    self.pool.remove(i)
                except ValueError:  # already removed by another thread
                    pass  # ignore, not an issue

        if len(self.pool) < self.poolSize:
            threading.Thread(target=self.fill).start()
        if len(self.pool) == 0:
            self.poolSize += 1 if self.poolSize < self.poolSizeLimit + 1 else 0
            self.inviteSize += 1 if self.inviteSize < self.inviteSizeLimit+1 else 0
            print("::InvitePool::  " + term.green(f"Inflating invite pool to {self.poolSize}"))
            print("::InvitePool::  " + term.green(f"Inflating invite size to {self.inviteSize}"))
        else:
            self.poolSize = self.poolSize - 1 if self.poolSize > self.poolSizeDefault else self.poolSizeDefault
            self.inviteSize = self.inviteSize - 1 if self.inviteSize > 1 else 1
            print("::InvitePool::  " + term.red(f"Deflating invite pool to {self.poolSize}"))
            print("::InvitePool::  " + term.red(f"Deflating invite size to {self.inviteSize}"))

    def fill(self):
        print("::InvitePool::  " + term.cyan4("Filling"))
        for i in range(self.poolSize - len(self.pool)):
            if len(self.pool) < self.poolSize:
                self.add()
            else:
                break
        print("::InvitePool::  " + term.cyan("Filled"))
        self.debug()

    def get(self):
        self.debug()
        print("::InvitePool::  " + term.reverse(term.green("Returning new invite")))
        threading.Thread(target=self.check).start()
        threading.Thread(target=self.fill).start()
        if len(self.pool) > 0:
            val = self.pool[0]
            val[2] -= 1
            threading.Thread(target=self.check).start()
            return val[0]
        else:
            time.sleep(10 / 3)
            return self.get()
