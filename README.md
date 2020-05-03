# AKB Discord bot
A Discord bot to browse AttackerKB.

# Inviting the bot
No need to host it yourself! 
The bot can be invited using [this link](https://discordapp.com/api/oauth2/authorize?client_id=701046523387183165&permissions=117760&scope=bot).
If you really want to deploy it youself, instructions are at the bottom.

## Why is the code on Github
So you guys can know what is running on your server and also so anyone can contribute.


# Commands
```
help              | Get help.
assessment  <id>  | Get an assessment by its unique ID.
cve <id>          | Get a CVE by its code. (CVE-YEAR-XXXX)
ping              | Pong!
query <keywords>  | Search topics using keywords.
topic <id>        | Get a topic by its unique ID.
user <username>   | Get a user's profile by its username.
```

# Deployment
If you want to deploy another instance of the bot for whatever reason, here is how to.

## Run from command line
```bash
# set enviroment variables
export AKB_TOKEN="xxxxxxxxxxxxxxxxxxx"
export AKB_API_KEY="xxxxxxxxxxxxxxxxxxx"
python main.py
```

## 🐳 Running with Docker
First build the image
```bash
docker build -t akb-discord-bot .
```

Then run the container placing in your discord token and AKB api key in the --env vars.
```bash
docker run --rm --env DISCORD_TOKEN='' --env AKB_API_KEY='' akb-discord-bot
```

# Credits
* Thanks to @kevthehermit for helping me simplify my tool using his [python library](https://github.com/kevthehermit/attackerkb-api)!
* Also, thank you to @Sam-Lane for the Docker implementation.

# Related projects
* [AttackerKB-Explorer](https://github.com/horshark/akb-explorer)
