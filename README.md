# DBWBot

[![PyPI](https://img.shields.io/badge/python-3.6-blue.svg)](https://pypi.python.org/pypi/discord.py/)

A simple open source Discord bot, built with Discord.py.

Built primary for students of BTH, but feel free to modify / use for inspo.

Requires python3.6+


Current functions:

* Change role of user to the corresponding role using `!studenttyp <Campus|Distans>` (either one)
* More to come!

----------------


To install, use
```console
sudo pip3 install -r requirements.txt
```

Before launch you must modify `data/config.json.txt` with your own <a href="https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token">discord bot token</a>,
and remove the file extension so it's only named `config.json`.

To run the bot, launch using
```python
python3.6 launch.py
```

Add the bot to your server using the following link: https://discordapp.com/api/oauth2/authorize?client_id=486241051019968544&permissions=268438560&scope=bot

If you're missing pip, do the following (debian):
```console
sudo apt-get install python3-pip
```


Crontab example:
```
*/5 * * * * su - dbwbot -c 'cd /home/dbwbot/dbwbot && /usr/bin/python3.6 launch.py'
```
