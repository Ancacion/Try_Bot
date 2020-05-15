import discord
from discord.ext import commands
import os

class listerner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.Cog.listener()
    #async def on_message(self, msg):
    #    if msg.content.endswith == 'macbook':
    #        await msg.channel.send('還想換筆電啊 owO')

        #if msg.content.startswith == 'macbook':
        #    await msg.channel.send('還想換筆電啊 owO')
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == '123':
            await message.channel.send('Message from {0.author}: {0.content}\n'.format(message))
        #for i in range(1):
        #if message.content.startswith('$hello'):
            #await message.channel.send('Message from {0.author}: {0.content}'.format(message)) 
            #print('hello')

        #if message.content.endswith == 'macbook':
            #await message.channel.send('{0.author}還想買{0.content}啊'.format(message)) 
            #print('hello')

def setup(bot):
    bot.add_cog(listerner(bot))