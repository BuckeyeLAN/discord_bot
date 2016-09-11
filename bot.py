import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!', description='The official BuckeyeLAN bot')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def commend():
	await bot.say('Added one point to !')
	return

@bot.command()
async def test():
	await bot.say('Test!')

@bot.command()
async def points():
	await bot.say(' has a total of xxx points!')
	return

@bot.command()
async def roulette(amount : int):
	return

@bot.command()
async def quote():
	return

@bot.command()
async def catgirl():
	catNumber = random.randint(1, 325)
	catName = catNumber
	if(catNumber >= 315):
		await bot.say("__***BONUS ROUND***__")
		bonusCatNumber = random.randint(1, 22)
		catName = 'BONUS' + str(bonusCatNumber)
	imageName = "CatgirlDB\\" + str(catName) + '.jpg'
	await bot.upload(imageName)
	return

@bot.command()
async def husbando():
	return

bot.run('MjI0MjM0MzUzMTcxODkwMTc3.CrYQfA.gA246SiyVTS_SICctEo-7JJKwRU')
