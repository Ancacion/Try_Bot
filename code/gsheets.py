from discord.ext import commands
import pygsheets
import json

with open('cmd.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)

gc = pygsheets.authorize(client_secret = data['gsheets'])

class gsheets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #新增表單
   # @commands.command()
   # async def newSheet(self, ctx):
   #     return 1 

    #開啟表單(測試中)
    @commands.command()
    async def openSheet(self, ctx):
        sh = gc.open('PythonTest')
        await ctx.send("Open PythonTest Successed!")
        wks = sh[0]
        A1 = wks.cell('A1')
        A2 = wks.cell('B1')
        await ctx.send(str(A1) + ' ' + str(A2))
        
def setup(bot):
    bot.add_cog(gsheets(bot))
