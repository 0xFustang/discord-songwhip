# discord-songwhip

A simple Discord bot to generate a Songwhip link.

[Songwhip](https://songwhip.com/) provides the ability to generate a link leading to majors platforms (Spotify, Apple Music, Tidal, and more).

This bot will provide the command `/music`. The users will need to provide any link from a track (could be YouTube) and the bot will provide a Songwhip link.

![Preview](./img.png)

## Installation

1. Add a bot on the desired server (https://discord.com/developers/applications) - (Required: "Send message");
2. Copy `Secrets.py.example` into `src/discord-songwhip/Secrets.py`, edit `Secrets.py` and provide:
    - `DISCORD_TOKEN` - Token of the Discord bot;
    - `DISCORD_GUILDID` - GuildID of the Discord server;
3. Setup the virtual enviromnent:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
    - `pip install --no-cache-dir -r requirements/discord-songwhip.txt`
3. Execute `python src/discord-songwhip/main.py`.

If you wish to make this bot running as a service, you can use the following `systemd` service file:

1. Create the file `/etc/systemd/system/botsong.service`
```
[Unit]
Description=BotSong - Songwhip
After=network.target

[Service]
Type=simple
User=doe
WorkingDirectory=/home/doe/discord-songwhip/
Environment=PYTHONPATH=/home/doe/discord-songwhip/
ExecStart=/home/doe/discord-songwhip/venv/bin/python /home/doe/discord-songwhip/src/discord-songwhip/main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

2. Reload systemd

```
$ sudo systemctl daemon-reload
```

3. Start and enable the service
```
$ sudo systemctl start botsong
$ sudo systemctl enable botsong
```

## Building a docker image

You can use this bot with a docker image. First, you need to `git clone` this project, copy `Secrets.py.example` into `Secrets.py` and provide the Token and the GuildID.

To build image, use command:
```
docker build -t discord-songwhip .
```

Then check if your image was built:

```
docker images
```

You should see:

```
REPOSITORY         TAG       IMAGE ID       CREATED          SIZE
discord-songwhip   latest    523ac10ad25b   19 seconds ago   932MB
```

To run `discord-songwhip` in Docker:

```
docker run -d discord-songwhip
```
