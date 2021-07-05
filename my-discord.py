#!/home/neosvr/toolbox/sysinfo/bin/python
# hack13's personal discord bot script
# ChangeLog
# June 3, 2021: Intial creation of the bot
# June 4, 2021: Adding moderation tooling for discord
# June 14, 2021: Cleaned up and made him speak a bit less sassy
# June 19, 2021: Switching to hide the actual important stuffs with dot_env
# July 4, 2021: Updating the bot to support using new API service, getting rid of the SSH stuff

import os
import time 
import json
import requests
from discord.ext import commands
# from dotenv import dotenv_values
from dotenv import load_dotenv

# Load in my environment vars
load_dotenv()
#config = dotenv_values(".env")
known_hosts = os.getenv('ssh_knownhosts')
hacksbox = os.getenv('hacksbox')
api_key = os.getenv('api_key')
neosapi = os.getenv('german_server')
TOKEN = os.getenv('token')

# Build out the API tooling
my_header = {'X-API-Key' : f'{api_key}'}

# Set ! as the command prefix
bot = commands.Bot(command_prefix='!')

## Events
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def on_member_join(ctx, member):
	welcome_message = f'Welcome to the server {member}!'
	await ctx.send(welcome_message)

## Commands
@bot.command(name='loveme', help='Something stupid because I can')
async def loveme(ctx):
	response = 'I am sorry... I wasn\'t programmed to love...'
	await ctx.send(response)

@bot.command(name='bsod', help='silly response')
async def bsod(ctx):
	response = 'I run on Linux, the only thing I am scared of is a kernel panic.'
	await ctx.send(response)

@bot.command(name='testing', help='some test for json response')
async def testing(ctx):
	jsondata = requests.get(f'http://{hacksbox}:5000/save', headers=my_header)
	parseit = jsondata.json()
	await ctx.send(parseit['state'])

@bot.command(name='shutup', help='some other stupid response')
async def shutup(ctx):
	response = 'You want me to what?! I am not going to shutup!\n *screams* AAAAAAAAAA!!!!! *screams*'
	await ctx.send(response)
	
@bot.command(name='headlesshelp', help='List of all the headless commands')
async def headlesshelp(ctx):
	response = " **!save <headless>**: Execute a save on the headless server\n **!shutdown <headless>**: Shutdown a headless server\n **!start <headless>**: Start a headless server\n **!restart <headless>**: Restarts a headless server\n **!patch <headless>**: Patch headless server\n **!invite <headless> <username>**: Invite user to headless server\n **!afr <headless> <username>**: Accept Friend Request of the headless user\n **!clearcache <headless>**: Stops, clears cache, and restarts a headless server"
	await ctx.send(response)
	
@bot.command(name='save', help='Used to save headless neos servers')
@commands.has_role('Headless Manager')
async def save(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/save', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/save', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='shutdown', help='Used to shutdown headless neos servers')
@commands.has_role('Headless Manager')
async def shutdown(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/stop', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/stop', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='start', help='Used to start headless neos servers')
@commands.has_role('Headless Manager')
async def start(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/start', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/start', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='restart', help='Used to restart headless neos servers')
@commands.has_role('Headless Manager')
async def restart(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/restart', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/restart', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='patch', help='Used to patch headless neos servers')
@commands.has_role('Headless Manager')
async def patch(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'{neosapi}:8880/patch', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/patch', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='clearcache', help='Used to clear cache on headless neos servers')
@commands.has_role('Headless Manager')
async def clearcache(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/clearcache', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/clearcache', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)
		
@bot.command(name='invite', help='Used to invite users to headless neos servers')
@commands.has_role('Headless Manager')
async def invite(ctx, headless, username):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/invite?username={username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/invite?username={username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='acceptfriendrequest', help='Used to accept friend requests of the headless user', aliases=['afr'])
@commands.has_role('Headless Manager')
async def acceptfriendrequest(ctx, headless, username):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'http://{neosapi}:8880/afr?username={username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'http://{hacksbox}:5000/afr?username={username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)
		
bot.run(TOKEN)