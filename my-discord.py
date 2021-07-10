# We need to import some things
import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

# Load in my environment vars
load_dotenv()
hacksbox = os.getenv('hacksbox')
voidsbox = os.getenv('voidsbox')
api_key = os.getenv('api_key')
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

## Commands
@bot.command(name='loveme', help='Something stupid because I can')
async def loveme(ctx):
	response = 'I am sorry... I wasn\'t programmed to love...'
	await ctx.send(response)

@bot.command(name='bsod', help='silly response')
async def bsod(ctx):
	response = 'I run on Linux, the only thing I am scared of is a kernel panic.'
	await ctx.send(response)

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
		jsondata = requests.get(f'https://{voidsbox}/save', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/save', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='focus', help='Used to change the focused world on headless server')
@commands.has_role('Headless Manager')
async def save(ctx, headless, focus):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/focus?world={focus}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/focus?world={focus}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='shutdown', help='Used to shutdown headless neos servers')
@commands.has_role('Headless Manager')
async def shutdown(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/stop', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/stop', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='start', help='Used to start headless neos servers')
@commands.has_role('Headless Manager')
async def start(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/start', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/start', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='restart', help='Used to restart headless neos servers')
@commands.has_role('Headless Manager')
async def restart(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/restart', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/restart', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='patch', help='Used to patch headless neos servers')
@commands.has_role('Headless Manager')
async def patch(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		await ctx.send('Patching the headless, this will take a moment.')
		jsondata = requests.get(f'https://{voidsbox}/patch', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		await ctx.send('Patching the headless, this will take a moment.')
		jsondata = requests.get(f'https://{hacksbox}/patch', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='clearcache', help='Used to clear cache on headless neos servers')
@commands.has_role('Headless Manager')
async def clearcache(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		await ctx.send('Clearing cache of the headless, this will take a moment.')
		jsondata = requests.get(f'https://{voidsbox}/clearcache', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		await ctx.send('Clearing cache of the headless, this will take a moment.')
		jsondata = requests.get(f'https://{hacksbox}/clearcache', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)
		
@bot.command(name='invite', help='Used to invite users to headless neos servers')
@commands.has_role('Headless Manager')
async def invite(ctx, headless, username):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/invite/{username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/invite/{username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='acceptfriendrequest', help='Used to accept friend requests of the headless user', aliases=['afr'])
@commands.has_role('Headless Manager')
async def acceptfriendrequest(ctx, headless, username):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/afr/{username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/afr/{username}', headers=my_header)
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='getmetric', help='Used to get a system metric from the headless...')
@commands.has_role('Headless Manager')
async def getmetric(ctx, headless, metric):
	if headless == 'voidsheadless' or headless == 'vh':
		jsondata = requests.get(f'https://{voidsbox}/sysinfo/{metric}')
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	elif headless == 'hacksheadless' or headless == 'hh':
		jsondata = requests.get(f'https://{hacksbox}/sysinfo/{metric}')
		parseit = jsondata.json()
		response = f'{parseit["name"]}: {parseit["state"]}'
		await ctx.send(response)
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

bot.run(TOKEN)