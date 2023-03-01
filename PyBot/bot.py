import discord
import responses
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@bot.command()
async def test(ctx):
    await ctx.send('Komanda povezana')



def run_discord_bot():
    TOKEN = 'MTA4MDU1OTkyNTc3NzkzMjMwOA.GCH9Cy.b0-EEwmOQIJOI4BFCijCSUklwc43zb9vEeZBtE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    client.run(TOKEN)
