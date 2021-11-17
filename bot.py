import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    def new_invite(self, channel):
        x = await self.get_channel(channel).create_invite(max_age=300,max_uses=1)
        print(x)
        return x

