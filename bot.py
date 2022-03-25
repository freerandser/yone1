import discord
from discord.ext import commands
import lol

bot = commands.Bot(command_prefix='@')  # 접두사가 '@'


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def hello(ctx):  # '$hello'라는 메시지를 보냈을 때 @이름 Hello!를 보내줌
    await ctx.send('{0.author.mention} Hello!'.format(ctx))


@bot.command(name='협곡')
async def random_lol(ctx, *, text=''):
    message = ''
    result = lol.getresult(text)
    for key, value in result.items():
        if value != '':
            message += key + ' : ' + value + '\n'
    await ctx.send(message)


access_token = os.environ["BOT_TOKEN"]
client.token(access_token)
