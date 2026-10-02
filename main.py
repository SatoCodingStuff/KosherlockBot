import discord
import os
from dotenv import load_dotenv
import db
import api

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is up!")\

@bot.command(description="Link your deadlock account")
async def link(ctx, steam_friend_code: discord.Option(str)):
    db.addUser(ctx.author.id, steam_friend_code)
    await ctx.respond("Linked!", ephemeral=True)

@bot.command()
async def getrank(ctx, user: discord.Member):
    deadlock_id = db.getDeadlockId(user.id)

    embed = discord.Embed(
        title = f"{user.name}'s Rank is {api.stylizedRank(api.getRank(deadlock_id), api.getSubrank(deadlock_id))}",
        description = "",
        color = discord.Colour.blurple(),
    )
    await ctx.respond(embed = embed)

@bot.command()
async def leaderboard(ctx):
    playerFieldText = ""
    rankFieldText = ""
    topTen = db.getTopTen()

    embed = discord.Embed(
        title = "KosherLock Ranked Leaderboard!",
        description = "",
        color = discord.Colour.blurple(),
    )

    i = 0
    while(i < 10):
        playerFieldText += f"{i + 1}. <@{topTen[i][0]}>\n"
        rankFieldText += f"**{api.stylizedRank(api.getRank(topTen[i][1]), api.getSubrank(topTen[i][1]))}**\n"
        i += 1

    embed.add_field(name = "\t", value = "\t", inline = True)
    embed.add_field(name = "", value = playerFieldText, inline = True)
    embed.add_field(name = "", value = rankFieldText, inline = True)

    await ctx.respond(embed = embed)

bot.run(os.getenv('TOKEN'))