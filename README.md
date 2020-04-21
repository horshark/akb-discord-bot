# AKB Discord bot
A Discord bot to browse AttackerKB.

# Hosting
The bot will soon be a public bot, hosted by myself.

# Deployment
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
docker run --rm --env DISCORD_TOKEN='' --env AKB_API_KEY='' akb-d
iscord-bot
```

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

# Credits
Thanks to @kevthehermit for helping me simplify my tool using his [python library](https://github.com/kevthehermit/attackerkb-api)!

# Related projects
* [AttackerKB-Explorer](https://github.com/horshark/akb-explorer)
