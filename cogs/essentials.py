import discord
from discord.ext import commands
from discord.utils import get
from tendo import singleton

import asyncio

# Prevent multiple instances
me = singleton.SingleInstance()

class Essentials(discord.Client):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def studenttyp(self, ctx, role_: str):
        """
        Command to choose student role.
        """
        role_ = role_.lower()
        role_ = role_.capitalize()
        role = role_

        member = ctx.message.author
        role = get(member.server.roles, name=role)
        if role is not None:
            print(f"Selected role =", role)
            if role_ == "Campus" or role_ == "Distans":
                await self.bot.add_roles(member, role)
                print(f"Added member to role.")
            else:
                print(f"Unauthorised role given!")
        else:
            print(f"Role does not exist!")

def setup(bot):
    bot.add_cog(Essentials(bot))
