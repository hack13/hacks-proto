#!/home/neosvr/toolbox/sysinfo/bin/python
# hack13's personal discord bot script
# ChangeLog
# June 3, 2021: Intial creation of the bot
# June 4, 2021: Adding moderation tooling for discord
# June 14, 2021: Cleaned up and made him speak a bit less sassy
# June 19, 2021: Switching to hide the actual important stuffs with dot_env

import os
import time 
from discord.ext import commands
from paramiko import SSHClient, AutoAddPolicy
from dotenv import dotenv_values

# Load in my environment vars
config = dotenv_values(".env")
known_hosts = config.ssh_knownhosts
ssh_user = config.ssh_user
ssh_key = config.ssh_key
headless_manager_path = config.headless_script
voidsbox = config.german_server
hacksbox = config.hacks_server
TOKEN = config.token

# Build out the SSH connection stuff
client = SSHClient()
client.load_system_host_keys()
client.load_host_keys(known_hosts)
client.set_missing_host_key_policy(AutoAddPolicy())

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
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} save')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} save')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='shutdown', help='Used to shutdown headless neos servers')
@commands.has_role('Headless Manager')
async def shutdown(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		await ctx.send('Ugh... give me a minute...')
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} shutdown')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		await ctx.send('Ugh... give me a minute...')
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} shutdown')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='start', help='Used to start headless neos servers')
@commands.has_role('Headless Manager')
async def start(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		await ctx.send('Ugh... give me a minute...')
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} start')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		await ctx.send('Ugh... give me a minute...')
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} start')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='restart', help='Used to restart headless neos servers')
@commands.has_role('Headless Manager')
async def restart(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		notice = 'This will take a couple minutes, please wait for me to let you know I am done.'
		await ctx.send(notice)
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} restart')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		notice = 'This will take a couple minutes, please wait for me to let you know I am done.'
		await ctx.send(notice)
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} restart')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='patch', help='Used to patch headless neos servers')
@commands.has_role('Headless Manager')
async def patch(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		notice = 'This will take a couple minutes, please wait for me to let you know I am done.'
		await ctx.send(notice)
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} patch')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		notice = 'This will take a couple minutes, please wait for me to let you know I am done.'
		await ctx.send(notice)
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} patch')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='clearcache', help='Used to clear cache on headless neos servers')
@commands.has_role('Headless Manager')
async def clearcache(ctx, headless):
	if headless == 'voidsheadless' or headless == 'vh':
		notice = 'This will take a couple minutes, please wait for me to let you know I am done.'
		await ctx.send(notice)
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} clearcache')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		notice = 'This will take a couple minutes, please wait for me to let you know I am done.'
		await ctx.send(notice)
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} clearcache')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)
		
@bot.command(name='invite', help='Used to invite users to headless neos servers')
@commands.has_role('Headless Manager')
async def invite(ctx, headless, username):
	if headless == 'voidsheadless' or headless == 'vh':
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} invite {username}')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} invite {username}')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)

@bot.command(name='acceptfriendrequest', help='Used to accept friend requests of the headless user', aliases=['afr'])
@commands.has_role('Headless Manager')
async def acceptfriendrequest(ctx, headless, username):
	if headless == 'voidsheadless' or headless == 'vh':
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} acceptfriendrequest {username}')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	elif headless == 'hacksheadless' or headless == 'hh':
		client.connect(voidsbox, username=ssh_user, key_filename=ssh_key)
		stdin, stdout, stderr = client.exec_command(f'{headless_manager_path} acceptfriendrequest {username}')
		response = f'{stdout.read().decode("utf8")} {stderr.read().decode("utf8")}'
		await ctx.send(response)
		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
	else:
		response = "I don't know that headless server..."
		await ctx.send(response)
		
bot.run(TOKEN)