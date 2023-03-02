import discord
import time
import responses
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), intents=intents)
CHANNEL_ID = 971388077148889159


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@bot.command()
async def test(ctx):
    await ctx.send('Komanda povezana')


@bot.event
async def on_message(message, member: discord.Member = None):
    if message.author == client.user:
        return
    if message.content.startswith('!test'):
        await message.channel.send('Bot je aktivan!')
    if message.content.startswith('!clanovi'):
        embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description='Clanovi CSGO grupe Kraj1na',
            title='Clanovi',

        )
        name = member.display_name
        pfp = member.display_avatar
        embed.set_author(f'{name}'),
        embed.set_footer(text='Kraj1na Strong'),
        await message.channel.send(embed=embed)


#9w
def run_discord_bot():
    TOKEN = 'MTA4MDU1OTkyNTc3NzkzMjMwOA.GjxMd4.K69pXMvP8r8CytVJiQalspZ0QXDTwI6I79ja'


    @client.event
    async def on_ready():
        print(f'{client.user} je spreman')
    client.run(TOKEN)
