from email import message

import discord
import responses

async def send_message(message, user_message, is_private):
	try:
		response = responses.handle_response(user_message)
		await message.author.send(response) if is_private else message.channel.send(response)
	except Exception as e:
		print(e)
def run_discord_bot():
	TOKEN = 'MTI1NjMyMzM5NDIyNDM5NDI3MQ.GzG-of.0WWH3CvY3ElJo0ltWz2d_VedqzGSj1Mco1w-c8'
	client = discord.Client(intents=discord.Intents.default())

	@client.event
	async def on_ready():
		print(f'{client.user} is now running')

	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
		username = str(message.author)
		user_message = str(message.content)
		channel = str(message.channel)

		print(f"{username} said: '{user_message}'({channel})")

		if user_message[0] == '?':
			user_message = user_message[1:]
			await send_message(message, user_message, True)
		else:
			await send_message(message, user_message, False)

	client.run(TOKEN)