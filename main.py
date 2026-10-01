import discord
import os
from dotenv import load_dotenv
import db

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is up!")\

@bot.command(description="Link your deadlock account")
async def link(ctx, steam_friend_code: discord.Option(str)):
    db.addUser(ctx.author.id, steam_friend_code)
    await ctx.respond("Linked!")

@bot.command()
async def embedtest(ctx):
    playerFieldText = ""
    rankFieldText = ""

    embed = discord.Embed(
        title = "KosherLock Ranked Leaderboard!",
        description = "",
        color = discord.Colour.blurple(),
    )

    embed.add_field(name = "", value = "**Player**", inline = True)
    embed.add_field(name = "", value = "**Rank**", inline = True)

    i = 1
    while(i <= 10):
        playerFieldText += "\n"
        rankFieldText += "\n"
        i += 1

    embed.add_field(name = "\t", value = "\t", inline = True)
    embed.add_field(name = "", value = playerFieldText, inline = True)
    embed.add_field(name = "", value = rankFieldText, inline = True)

    await ctx.respond(embed = embed)

bot.run(os.getenv('TOKEN'))