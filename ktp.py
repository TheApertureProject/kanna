botversion = 'v1.1.2 TAP build'
# |bot info
# |Username : Kanna#6715
# ¦ID :  467332623677521940
# |Invite link : https://discordapp.com/oauth2/authorize?client_id=467332623677521940&scope=bot&permissions=2146958591
# ¦Maintenance server link : https://discord.gg/PTT9UpZ

print("___________________________________________________")
print("""
            _  __                    _  
           | |/ /__ _ _ _  _ _  __ _| | 
           | ' </ _` | ' \| ' \/ _` |_| 
           |_|\_\__,_|_||_|_||_\__,_(_) 
""")
print("             The Kawaii Discord bot !           ")
print("                                                   ")
print("                 "+botversion+"                      ")
print("                                                   ")
print("___________________________________________________")
print()
import os
print(('[' + ctime()) + "] Lib 'os' successfully imported !")
import time
from time import *
print(('[' + ctime()) + "] Lib 'time' successfully imported !")
import datetime
from datetime import *
print(('[' + ctime()) + "] Lib 'datetime' successfully imported !")
import random
from random import *
print(('[' + ctime()) + "] Lib 'random' successfully imported !")
import sys
from sys import exit, version
print(('[' + ctime()) + "] Lib 'sys' [exit, version] successfully imported !")
import discord
from discord.ext import commands
print(('[' + ctime()) + "] Lib 'discord' successfully imported !")
print(('[' + ctime()) + '] Establishing connection with the bot...')
bot = commands.Bot(description='Kanna - The Kawaii Discord bot - Server management bot ©2018 Poulpe#2356', command_prefix='k!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print(('[' + ctime()) + '] Connection successfully established with the bot user :', bot.user.name)
	print('Bot user ID :', bot.user.name)
	await bot.change_presence(activity=discord.Game(name='k!help'))
	print(('[' + ctime()) + '] Presence successfully updated !')
	print('___________________________________________________')

@bot.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, name='Cuties')
	role2 = discord.utils.get(member.guild.roles, name='▬▬▬▬▬▬Profil▬▬▬▬▬▬▬')
	role3 = discord.utils.get(member.guild.roles, name='▬▬▬▬▬▬Hobbies▬▬▬▬▬▬')
	role4 = discord.utils.get(member.guild.roles, name='▬▬▬▬▬Jeux-vidéos▬▬▬▬▬')
	await member.add_roles(role, role2, role3, role4)
	await member.send(f"""tohru.exe et moi te souhaitons la bienvenue, **{member.display_name}** ! Je t'ai attribué tous les rôles nécéssaires à ta bonne intégration sur notre serveur.

	| Nous disposons d'un **système de rôle auto-attribuables par l'utilisateur**, donc n'hésite pas à jeter un oeil dans <#466643001066782721>, <#466643077122097153> et <#466643030246424597> pour les obtenir !
	| Le channel <#467021094793117707> est à ta disposition pour en dire un peu plus sur toi !
	| Et enfin, n'oublie pas de check <#466629126325927936> et <#466629153291239435> **pour encore mieux connaître notre serveur et ses règles** !
	
Tohru et moi espérons que tu apprécieras ton séjour sur notre merveilleux serveur !

	| Invite de notre serveur : https://discord.gg/HnMBzJn
```Markdown
#Not french ? No worries ! Just type -role Multi-Lingual anywhere into the server to access to the english category :3```
```Coded by tohru.exe#9355 ^^```""")
	my_guild = bot.get_guild(466600971213209600)
	join = my_guild.get_channel(466600971213209602)
	await join.send(f"Bienvenue, {member.mention} ! Merci de vérifier tes messages privés, je t'ai envoyé tout le nécéssaire pour mieux maîtriser notre serveur... Nous espérons que tu te plairas ici !")

@bot.event
async def on_member_remove(member):
	my_guild = bot.get_guild(466600971213209600)
	quit = my_guild.get_channel(466603496322498561)
	await quit.send(f"On dirait que {member.display_name} a quitté le serveur... Au revoir, et n'oublie pas que tu es toujours le bienvenu parmi nous ! *Sauf si tu t'es lamentablement fait ban, auquel cas je ne peux rien faire pour toi, désolée !*")

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("Je suis désolée, mais vous n'avez pas les permissions requises...")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.say("Membre spécifié incorrect ou inexistant. Réessayez, s'il vous plaît !")
	elif isinstance(error, commands.InvalidArgument):
		await ctx.say("Membre spécifié incorrect ou inexistant. Réessayez, s'il vous plaît !")

@bot.listen()
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.add_reaction('❌')

def is_owner(ctx):
	if ctx.author.id == 458586186328571913:
		return True
	else :
		return False

@bot.command()
async def help(ctx):
	e = discord.Embed(description="Commandes de base", title='Page 1', color=0x00FFC0, timestamp=datetime.utcnow())
	e.add_field(name='help', value='Affiche ce message')
	e.add_field(name='info', value='Apprenez-en plus sur moi ! :D')
	e.add_field(name='ping', value='Testez ma réactivité')
	e.add_field(name='suggest <suggestion>', value='Suggérez-nous vos idées pour le bot avec cette commande.')
	e.add_field(name='bugreport <bug>', value ='Signalez-nous des bugs trouvés sur Kanna via cette commande.')
	a = discord.Embed(description="Commandes de modération", title='Page 2', color=0x00FF80, timestamp=datetime.utcnow()) 
	a.add_field(name='kick <member/id>', value="Excluez un utilisateur du serveur.")
	a.add_field(name='ban <member/id> <reason>', value="Excluez définitivement un utilisateur du serveur.")
	a.add_field(name='clear <amount of messages>', value='Supprimez un nombre précis de messages - Pas de limites ! Soyez prudent :3')
	a.add_field(name='De nouvelles commandes sont en préparation et arriveront bientôt !', value='💠')
	c = discord.Embed(description='Utilitaires', title='Page 3', color=0x00FF40, timestamp=datetime.utcnow())
	c.add_field(name='pp <user>', value="Obtenez la photo de profil d'un utilisateur du serveur")
	d = discord.Embed(description='Fun', title='Page 4', color=0xFFA2DD, timestamp=datetime.utcnow())
	d.add_field(name='coolservs', value='Just take a look on our other servers !')
	d.add_field(name='Other cool and fun commands are coming !', value='Hang on a little~')
	await ctx.send(embed=e)
	await ctx.send(embed=a)
	await ctx.send(embed=c)
	await ctx.send(embed=d)
	if ctx.author.id == 458586186328571913 :
		b = discord.Embed(description='Master commands ♥️', title='Page ♾️', color=0xFF0000, timestamp=datetime.utcnow())
		b.add_field(name='say <channel> <text>', value='Talk through me !')
		b.add_field(name='shutdown', value='Shut me down...')
		await ctx.send(embed=b)

@bot.command()
async def invite(ctx):
	await ctx.send("Voici mon lien d'invitation ! merci de m'avoir ajoutée ♥")
	await ctx.send('<https://bit.ly/2KCvxDw>')

@bot.command()
async def pp(ctx, usr: discord.User):
	e = discord.Embed(description="Image de profil de {}".format(usr.name), title='Avatar', color=0x5D5DFF, timestamp=datetime.utcnow())
	e.set_image(url=usr.avatar_url)
	await ctx.send(embed=e)

@bot.command()
async def coolservs(ctx):
	e = discord.Embed(description="Nicu servers 👌", title='Discover other places', color=0xFFFFFF, timestamp=datetime.utcnow())
	e.add_field(name='The Aperture Project', value='A nice place to chill out and have fun, with giveaways, kawaii pics and a super friendly community ! https://discord.gg/JEUUM8c')
	e.add_field(name="Sebis's bot Tutorial", value='The best server to learn how to code bots in different languages ! https://discord.gg/GWdhBSp')
	await ctx.send(embed=e)

@commands.check(is_owner)
@bot.command(pass_context=True)
async def say(ctx, channel: discord.TextChannel, *, text):
	'Talk through me.'
	try:
		await channel.send(text)
	except Exception as e:
		print(e.args)

@say.error
async def say_handler(ctx, err):
	if isinstance(err, commands.CheckFailure):
		await ctx.send('Mes excuses, mais seul tohru.exe peut utiliser cette commande !')
	else:
		raise err

@commands.check(is_owner)
@bot.command()
async def shutdown(ctx):
	'Completely shut Kanna down.'
	try:
		await ctx.send('Compris !')
		await ctx.send('Arrêt en cours...')
		await ctx.send('Au revoir !')
		print(('[' + ctime()) + '] Succesfully shutted down.')
		sys.exit()
	except Exception as e:
		print(e.args)
		await ctx.send("Une erreur est survenue... Vérifiez les journaux système, je suis sûre que ce n'est rien !")

@shutdown.error
async def shutdown_handler(ctx, err):
	if isinstance(err, commands.CheckFailure):
		await ctx.send("Accès refusé. Vous n'êtes pas tohru.exe !")
	else:
		raise err

@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, member: discord.Member, *, reason: str = None):
	'Ban a member from the server.'
	try:
		if reason==None:
			await member.ban()
		else:
			await member.ban(reason=reason)
		await ctx.send('{} a été banni avec succès. Au revoir :3'.format(member))
	except Exception as e:
		print(e.args)
		await ctx.send("Une erreur est survenue. Auriez-vous mal saisi le nom d'utilisateur ?")

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, member: discord.Member):
	'Kick a member from the server.'
	try:
		await member.kick()
		await ctx.send('{} a été exclu avec succès. Babaï~'.format(member))
	except Exception as e:
		print(e.args)
		await ctx.send("Une erreur est survenue. Auriez-vous mal saisi le nom d'utilisateur ?")

@commands.has_permissions(manage_messages=True)
@bot.command()
async def clear(ctx, amount: int):
	amount=amount+1
	if amount != 0:
		try:
			deleted = await ctx.channel.purge(limit=amount)
			await ctx.send(f"{len(deleted)} messages supprimés avec succès.", delete_after = 5)
		except:
			await ctx.send("La quantité de messages doit être constituée uniquement de nombres entiers positifs.")
	else:
		await ctx.send('La quantité de messages ne peut être égale à zéro :3')

@kick.error
async def kick_handler(ctx, err):
	if isinstance(err, commands.has_permissionsFailure):
		await ctx.send('Huh ?! Tu essayes de faire quoi, là ? Accès refusé !')
	else :
		raise err

@bot.command()
async def info(ctx):
	'Get to know me !'
	e = discord.Embed(description="Kanna, the Kawaii Discord bot - The Aperture Project edition", title='En savoir plus', color=0xF4A2FF, timestamp=datetime.utcnow())
	e.add_field(name='Programmé par', value='tohru.exe#9355')
	e.add_field(name="Lien d'ajout", value='https://bit.ly/2KCvxDw')
	e.add_field(name='Serveur de maintenance', value='https://discord.gg/PTT9UpZ')
	e.add_field(name='En fonctionnement sur Python {}'.format(discord.__version__), value=version)
	e.set_footer(text=botversion)
	e.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
	await ctx.send(embed=e)

@bot.command()
async def bugreport(ctx, *, bug):
	"Report a bug or error that you saw with Kanna. Your report will be sent to the Kanna's Server !"
	my_guild = bot.get_guild(462871882916560896)
	bugreport = my_guild.get_channel(462876207097053195)
	e = discord.Embed(description=bug, title='Bug Report', color=16711680, timestamp=datetime.utcnow())
	e.set_footer(text='Kanna - The Kawaii Discord bot')
	e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	await bugreport.send(embed=e)
	await ctx.send("Un bug ? ... tohru.exe devrait s'occuper de ça rapidement, merci du signalement !")

@bot.command()
async def suggest(ctx, *, suggestion):
	"Any idea of how could we improve Kanna ? Just use this command to suggest ideas ! Your suggestion will be sent to the Kanna's Server !"
	my_guild = bot.get_guild(462871882916560896)
	suggested = my_guild.get_channel(464517370036224011)
	e = discord.Embed(description=suggestion, title='Suggestion', color=4259584, timestamp=datetime.utcnow())
	e.set_footer(text='Kanna - The Kawaii Discord bot')
	e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	await suggested.send(embed=e)
	await ctx.send('Suggestion envoyée ! Merci beaucoup :3')

@bot.command()
async def ping(ctx):
	'Get the ping time of the bot.'
	t = await ctx.send('Pong!')
	ms = (t.timestamp - ctx.message.timestamp).total_seconds() * 1000
	await t.edit(new_content='Pong! Latence : **{} milliseconds** !'.format(int(ms)), content='Pong! Latency : **{} milliseconds** !'.format(int(ms)))

bot.run(bot.run(os.environ['TOKEN']))