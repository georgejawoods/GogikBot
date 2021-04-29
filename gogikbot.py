import discord # import discord
import asyncio
from discord.ext import commands

import emoji

import json
import requests
import os
import platform

from pyowm import OWM # import Open Weather Map 
from pyowm.utils import config
from pyowm.utils import timestamps

from config import settings# import basic settings for bot 

from random import randrange, shuffle
import time

if platform.system() == 'Linux':
	os.chdir("/mnt/d/MyProjects/gogikBot")
else:
	os.chdir("D:\\MyProjects\\gogikbot")

client = discord.Client()

bot = commands.Bot(command_prefix=settings['prefix'])# set prefix

@bot.event
async def on_ready():
	print('Ready!')

@bot.command() # command for reply to author of message 
async def hello(ctx):
	author=ctx.message.author

	await ctx.send(f'Hello, {author.mention}')

@bot.command() # check for ping bot
async def ping(ctx):
	await ctx.send('pong')

@bot.command() # see the temperature in the city
async def temp(ctx, arg1: str=0, arg2: str=0):
	owm = OWM('f2ffd8882106c2402a57aac7f78d5218') # call OWM
	mgr = owm.weather_manager()

	if arg1 + arg2 == 0:
		observation = mgr.weather_at_place('Nizhniy Novgorod')
		w = observation.weather
		temp = w.temperature('celsius')['temp']
		if int(temp) > 0: # show temperature of city
			await ctx.send(f'Temperature in Nizhniy Novgorod is: +{int(temp)}°C')
		else:
			await ctx.send(f'Temperature in Nizhniy Novgorod is: {int(temp)}°C') 
		
	else:
		if arg2 == 0:
			observation = mgr.weather_at_place(arg1)
			w = observation.weather
			temp = w.temperature('celsius')['temp']
			if int(temp) > 0: # show temperature of city
				await ctx.send(f'Temperature in {arg1} is: +{int(temp)}°C')
			else:
				await ctx.send(f'Temperature in {arg1} is: {int(temp)}°C') 
			
		else :
			arg1 += " " + arg2

			observation = mgr.weather_at_place(arg1)
			w = observation.weather
			temp = w.temperature('celsius')['temp']
			if int(temp) > 0: # show temperature of city
				await ctx.send(f'Temperature {arg1} is: +{int(temp)}°C')
			else:
				await ctx.send(f'Temperature {arg1} is: {int(temp)}°C') 

@bot.command() # show picture with red panda
async def rpanda(ctx):
	response = requests.get('https://some-random-api.ml/img/red_panda') # get red panda 
	json_data = json.loads(response.text)

	embed = discord.Embed(color = 0xFF0000, title = 'Random Red Panda') # Create Embed
	embed.set_image(url = json_data['link']) # add a picture
	await ctx.send(embed = embed)

@bot.command()# show picture with cat
async def cat(ctx):
	response = requests.get('https://some-random-api.ml/img/cat') # get cat 
	json_data = json.loads(response.text)

	embed = discord.Embed(color = 0xFF0000, title = 'Random Cat') # Create Embed
	embed.set_image(url = json_data['link']) # add a picture
	await ctx.send(embed = embed)

@bot.command()# show picture with dog
async def dog(ctx):
	response = requests.get('https://some-random-api.ml/img/dog') # get dog 
	json_data = json.loads(response.text)

	embed = discord.Embed(color = 0xFF0000, title = 'Random Dog') # Create Embed
	embed.set_image(url = json_data['link']) # add a picture
	await ctx.send(embed = embed)

@bot.command()# show picture with fox
async def fox(ctx):
	response = requests.get('https://some-random-api.ml/img/fox') # get fox 
	json_data = json.loads(response.text)

	embed = discord.Embed(color = 0xFF0000, title = 'Random Fox') # Create Embed
	embed.set_image(url = json_data['link']) # add a picture
	await ctx.send(embed = embed)

@bot.command() # random int
async def rand(ctx, arg: int=10):
	x = random.randrange(0, arg)
	await ctx.send(x)

@bot.command() # flip coin
async def coin(ctx):
	Coin = ['Tails', 'Heads']
	shuffle(Coin)
	await ctx.send(Coin[0])

@bot.command() # ban user
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}')

@bot.command() # unban user
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
			return

@bot.command() #clear chat
async def clear(ctx, amount=5):
	amount += 1
	await ctx.channel.purge(limit=amount)
	amount -= 1
	msg = await ctx.send(f'Deleted {amount} messages!')
	await asyncio.sleep(3)
	await msg.delete()


bot.run(settings['token']) # use token for bot
