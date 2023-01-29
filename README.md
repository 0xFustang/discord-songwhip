# discord-songwhip

A simple Discord bot that uses Songwhip to share a multi-platform music link.

For a given music track, [Songwhip](https://songwhip.com/) provides a single link where you can find the track on majors platforms (Spotify, Apple Music, Tidal, and more).

This bot offers the command `/music` where a user provides in the `link` argument any links from a track and return a Songwhip link.

## Bot setup

1. Add a bot on the desired server (https://discord.com/developers/applications) - (Required: "Send message");
2. Copy `Secrets.py.example` into `Secrets.py` and fill the values:
    - `DISCORD_TOKEN` - Token of the Discord bot;
    - `DISCORD_GUILDID` - GuildID of the Discord server;
3. Setup the virtual enviromnent:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
3. Launch `discord-songwhip.py`.