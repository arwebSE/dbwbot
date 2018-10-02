import sys
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from selenium import webdriver
#driver = webdriver.Chrome()

class Essentials(discord.Client):
    def __init__(self, bot):
        self.bot = bot
        #remove default command
        bot.remove_command('help')

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

    @commands.command(pass_context=True)
    async def dbwbot(self, ctx, *args: str):
        """Shows this message."""
        return await commands.bot._default_help_command(ctx, *args)

    # @commands.command(pass_context=True)
    # async def dbwcal(self, ctx):
    #     """Screenshot."""
    #     driver.get('https://www.spotify.com')
    #     screenshot = driver.save_screenshot('my_screenshot.png')
    #     driver.quit()
    #     print(f"screenshot saved.")
    #     return " "

def setup(bot):
    bot.add_cog(Essentials(bot))
