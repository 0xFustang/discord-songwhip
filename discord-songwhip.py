import discord
import Secrets
import requests
import json
import validators
import asyncio
import datetime


from discord import app_commands

async def requests_songwhip(link):

    url = 'https://songwhip.com/' # Songwhip URL
    input = {'url': link}
    r = requests.post(url, json = input)
    json_data = json.loads(r.text)
    songwhip_link = json_data['url']

    return songwhip_link


def discord_songwhip():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    @tree.command(name = "music", description = "Share a multi-platform music track!", guild=discord.Object(id=Secrets.DISCORD_GUILDID))
    @app_commands.describe(link="Provide a link from a song (.e.g YouTube, Spotify, Tidal link)")
    async def music(interaction, link: str):
        if validators.url(link):
            await interaction.response.defer()
            try:
                res = await requests_songwhip(link)
                await interaction.followup.send(res)
            except KeyError:
                await interaction.followup.send("Songwhip could not create a link using the provided url.")
            except:
                await interaction.followup.send("Something went wrong...")
        else:
            await interaction.response.send_message("I am terribly sorry but this is not a link! Post a link, any link!\nIt could be a YouTube link or a Spotify link for instance.", ephemeral=True)
    @client.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=Secrets.DISCORD_GUILDID))
        print("Ready!")

    client.run(Secrets.DISCORD_TOKEN)

if __name__ == '__main__':
    discord_songwhip()