# DBWBot

Simple open source Discord bot, built with Discord.py

To install, use
```console
sudo pip3 install -r requirements.txt
```

Before launch you must modify `data/config.json.txt` with your own <a href="https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token">discord bot token</a>,
and remove the file extension so it's only named `config.json`.

To run the bot, launch using
```python
python3 launch.py
```

Add the bot to your server using the following link: https://discordapp.com/api/oauth2/authorize?client_id=486241051019968544&permissions=268438560&scope=bot

If you're missing pip, do the following (debian):
```console
sudo apt-get install python3-pip
```
