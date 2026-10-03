import discord
import os
import db
import api
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is up!")
    updateLeaderboard.start()

# Taken the top 10 players and orginized them in embed format.
def enterLeaderboardFields(embed, playerFieldText, rankFieldText, topTen):
    i = 0
    while(i < 2):
        playerFieldText += f"{i + 1}. <@{topTen[i][0]}>\n"
        rankFieldText += f"**{api.stylizedRank(api.getRank(topTen[i][1]), api.getSubrank(topTen[i][1]))}**\n"
        i += 1

    embed.add_field(name = "\t", value = "\t", inline = True)
    embed.add_field(name = "", value = playerFieldText, inline = True)
    embed.add_field(name = "", value = rankFieldText, inline = True)

# Links steam account to discord account.
@bot.command(description="Link your deadlock account")
async def link(ctx, steam_friend_code: discord.Option(str)):
    db.addUser(ctx.author.id, steam_friend_code)
    await ctx.respond("Linked!", ephemeral=True)

# Sends an embed showing the rank of a given player.
@bot.command(escription="Shows the rank of a given user")
async def getrank(ctx, user: discord.Member):
    deadlock_id = db.getDeadlockId(user.id)

    embed = discord.Embed(
        title = f"{user.name}'s Rank is {api.stylizedRank(api.getRank(deadlock_id), api.getSubrank(deadlock_id))}",
        description = "",
        color = discord.Colour.blurple(),
    )
    await ctx.respond(embed = embed)

# Starts the leaderboard message.
# Should only be ran once and have its message id copied to 
# the update leaderboard function. 
@bot.command()
@commands.has_any_role("Vampire society", 1554925366743933078)
async def leaderboard(ctx):
    playerFieldText = ""
    rankFieldText = ""
    topTen = db.getTopTen()

    embed = discord.Embed(
        title = "KosherLock Ranked Leaderboard!",
        description = "",
        color = discord.Colour.blurple(),
    )

    enterLeaderboardFields(embed, playerFieldText, rankFieldText, topTen)

    await ctx.respond(embed = embed)

# Updates the leaderboard message.
@tasks.loop(seconds=3)
async def updateLeaderboard():
    channel_id = "1555855369115275324"
    message_id = "1555866017157091329"
    playerFieldText = ""
    rankFieldText = ""
    topTen = db.getTopTen()

    channel = await bot.fetch_channel(int(channel_id))
    message = await channel.fetch_message(int(message_id))
    embed = message.embeds[0]

    embed.clear_fields()

    enterLeaderboardFields(embed, playerFieldText, rankFieldText, topTen)
    await message.edit(embed=embed)

bot.run(os.getenv('TOKEN'))