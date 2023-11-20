import discord
import os

client = discord.Client(intents=discord.Intents(messages=True, reactions=True))

@client.event
async def on_ready():
	print("ログインが完了しました！")

@client.event
async def on_reaction_add(reaction, user):
	if str(reaction.emoji) == "😁":
		smile_url = "https://em-content.zobj.net/source/twitter/376/beaming-face-with-smiling-eyes_1f601.png"
		smile_embed = discord.Embed().set_image(url=smile_url)
		await reaction.message.reply("😁", embed=smile_embed)
		
client.run(os.getenv("TOKEN"))