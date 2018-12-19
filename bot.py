# Work with Python 3.6
import discord
from discord.ext.commands import Bot

from config import TOKEN, COMMAND_PREFIX

client = discord.Client()
bot = Bot(command_prefix=COMMAND_PREFIX)


@bot.command(pass_context=True)
async def play(ctx, arg=None):
    author = ctx.message.author
    voice_channel = author.voice_channel

    if not arg:
        await bot.say('Usage: !play <url>')
        return

    await bot.say('Downloading please wait..')
    try:
        vc = await bot.join_voice_channel(voice_channel)
        player = await vc.create_ytdl_player(arg)
    except:
        await bot.say('Error. If already playing, !stop first or check url.')
        return

    try:
        await bot.say('Playing: %s' % player.title)
        player.start()
    except:
        await bot.say('Unknown error. Please retry command or restart bot.')


@bot.command(pass_context=True)
async def stop(ctx, arg=None):
    for x in bot.voice_clients:
        if x.server == ctx.message.server:
            return await x.disconnect()


@bot.event
async def on_ready():
    print('Logged in as\n{0} {1}\n------'.format(bot.user.name, bot.user.id))

bot.run(TOKEN, bot=True)
