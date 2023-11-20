import discord
import os

client = discord.Client(intents=discord.Intents(messages=True))

@client.event
async def on_ready():
	print("ログインが完了しました！")
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await message.reply("こんにちは！" + message.author.name + "さん")
	
client.run(os.getenv("TOKEN"))