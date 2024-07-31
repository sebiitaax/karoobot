
import json, os
from discord.ext import commands
import discord
from discord.ext.commands import has_any_role


class Welcome_Embed():
	def __init__(self, member):
		# Member = nickname del nuevo usuario
		self.member = member


	@property
	def enviar(self):
		self.embed = discord.Embed(title=f"Hola {self.member}. Para unirte a la tripulación y ser un visitante/mugiwara más debes aceptar las siguientes reglas...", colour=int("DC75FF", 16))
		self.embed.add_field(name="Reglas del ☀𝕊𝕖𝕟𝕔𝕙𝕠̄👒☀:", value="1. No seas chistosito y no spamees. / 2. No abuses si se te otorga el permiso de mutear y ensordecer. / 3. Son pocas reglas, pero realmente el castigo el ☀𝕊𝕖𝕟𝕔𝕙𝕠̄👒☀ te lo dará según crea conveniente. ", inline=False)
		self.embed.add_field(name="Escribe el siguiente comando si estas de acuerdo en unirte a la tripulación:", value="!acepto", inline=False)
		return self.embed
	


def main():

	def create_config_archive():
		template = {
		'prefix': '!', 
		'token': "MTI2Nzk4NzE3Mzk5NTU4MTQ0MA.GRHmgH.f0bAG1BU9QqZbjI-8UjxiWdMyfXsM1zjpcMdvU", 
		}
		with open('config.json', 'w') as f:
			json.dump(template, f)


	def read_config_archive():
		with open('config.json') as f:
			config_data = json.load(f)
		return config_data


	if not os.path.exists('config.json'):
		print('Creando archivo de configuración')
		create_config_archive()


	# Parametros iniciales
	config_data = read_config_archive()
	prefix = config_data["prefix"]
	token = config_data["token"]
	intents = discord.Intents.all()
	bot = commands.Bot(
		command_prefix = prefix, 
		intents = intents, 
		description = "Bot moderador")


	# Comandos

	@bot.command(name='acepto', help='Te agrega el rol "usuario"')
	async def add_user_role(ctx):
		# Condicional para que este comando solo se ejecute en MD
		if isinstance(ctx.channel, discord.channel.DMChannel):
			# Obtenemos nuestro servidor mediante la ID
			server = bot.get_guild(1267949315150577795)
			# Obtenemos el rol de usuario de nuestro servidor
			rol = server.get_role(1267980882464215051)
			# Obtenemos al usuario de nuestro servidor mediante su id (la cual viene en el contexto) 
			member = server.get_member(ctx.message.author.id)
			# Le asignamos el rol
			await member.add_roles(rol)
			# Le enviamos un mensaje de bienvenida al servidor
			await ctx.author.send('Te has unido a la tripulación... DISFRUTA DE ESTE MOMENTO CON TUS NAKAMAS.')


	# Eventos
	@bot.event
	async def on_member_join(member):
		# ID del canal de bienvenida
		welcome_channel = bot.get_channel(1267963257365205032)
		# Usamos la plantilla para crear la respuesta
		welcome_embed = Welcome_Embed(member.name)
		# Enviamos el embed
		await member.send(embed = welcome_embed.enviar)
		# Damos la bienvenida
		await welcome_channel.send(f'¡Bienvenido al IMPRESIONANTE BARCO DEL PRÓXIMO REY DE LOS PIRATAS, {str(member.mention)}. Revisa tus mensajes privados para aceptar las normas y poder acceder a los demás canales!')


	@bot.event
	async def on_ready():
		activity = discord.Game(name="Tomar juguito preparado por Sanji.")
		await bot.change_presence(activity=activity)
		print('El bot esta funcionando correctamente.')


	bot.run(token)


if __name__ == '__main__':
	main()