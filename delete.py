import discord
import os

client = discord.Client(intents=discord.Intents(messages=True, message_content=True))

@client.event
async def on_ready():
    print("ログインが完了しました！")

@client.event
async def on_message_delete(message):
	await message.channel.send("メッセージを削除しましたね？\n" + message.content)
	
client.run(os.getenv("TOKEN"))