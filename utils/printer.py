import discord

author = "AttackerKB"
author_img = "https://attackerkb.com/static/public/img/favicon/favicon-32x32.png"
footer = "Made with \u2764 by @horshark"
color = 0x000000
base_url = "https://attackerkb.com/"

tags_desc = {
    "common_enterprise":"Common in enterprise environments",
    "default_configuration":"Present in the default configuration of the software",
    "requires_interaction":"Requires user interaction to exploit",
    "obscure_configuration":"Only present in an obscure configuration of the software",
    "difficult_to_exploit":"requires physical access or other high barriers to exploitation",
    "pre_auth":"Authentification not required to exploit",
    "post_auth":"Requires user interaction to exploit",
    "no_useful_data":"Does not give attackers access to useful data or footholds",
    "difficult_to_develop":"Difficult to develop PoC exploits for",
    "difficult_to_patch":"Difficult to patch or mitigate",
    "high_privilege_access":"Gives attackers high-privileged access quickly",
    "easy_to_develop":"Easy to develop PoC exploits for",
    "attacker_value":"Attacker Value",
    "exploitability":"Exploitability"
}

maxLenTitle = 15
maxLenDesc = 100

def topic(data):
    title = data["name"]
    desc = data["document"]
    
    if len(desc) > maxLenDesc*5:
        desc = desc[:maxLenDesc*5] + "[...]"

    response = discord.Embed(title=title, description=desc, color=color, url="")
    response.set_author(name=author, icon_url=author_img)
    response.set_footer(text=footer)

    data_tag = data['tags']

    items = {
        "Date":data["created"][0:10],
        "Link":"https://attackerkb.com/topics/"+data["id"],
        "Editor Id":data["editorId"],
        "Score":"AV: "+str(round(data["score"]["attackerValue"], 1)) + "\nExp: "+str(round(data["score"]["exploitability"], 1)),
        "High value":"Enterprise: "+str(round(data_tag['commonEnterprise'], 1)) + 
        "\nDefault config: "+str(round(data_tag['defaultConfiguration'], 1)) +
        "\nPatch difficulty: "+str(round(data_tag['difficultToPatch'], 1))+
        "\nhigh priv: "+str(round(data_tag['highPrivilegeAccess'], 1)) + 
        "\nEasy dev: "+str(round(data_tag['easyToDevelop'], 1)) +
        "\nNo auth: "+str(round(data_tag['preAuth'], 1)),
        "Low value":"Requires interation: "+str(round(data_tag['requiresInteraction'], 1)) +
        "\nObscure config: "+str(round(data_tag['obscureConfiguration'], 1)) + 
        "\nExp. difficulty: "+str(round(data_tag['difficultToExploit'], 1)) +
        "\nNo useful data: "+str(round(data_tag['noUsefulData'], 1))+
        "\nDifficult dev: "+str(round(data_tag['difficultToDevelop'], 1)) + 
        "\nNeeds auth: "+str(round(data_tag['postAuth'], 1))
    }

    for i in items:
        response.add_field(name=i, value=items[i])

    return response

def topic_list(query, data, length):
    title = "Query search"
    desc = str(length) + " first topics for " + query + ":"
    url = base_url

    response = discord.Embed(title=title, description=desc, color=color, url=url)
    response.set_author(name=author, icon_url=author_img)
    response.set_footer(text=footer)

    for i in range(length):
        title = data[i]["name"]
        desc = data[i]["document"]

        if len(title) > maxLenTitle:
            title = title[:maxLenTitle] + "[...]"

        if len(desc) > maxLenDesc:
            desc = desc[:maxLenDesc] + "[...]"

        response.add_field(name=title, value=desc)

    return response

def assessment(data, author_name, topic_name):
    desc = data["document"]
    permalink = base_url + "/assessments/" + data["id"]
    tags = ""

    if len(desc) > maxLenDesc*5:
        desc = desc[:maxLenDesc*5] + "[...]"


    data_tags = data["metadata"]['tags']
    tags_len = len(data_tags)

    for i in range(tags_len):
        tags += tags_desc[data_tags[i]]

        if i != tags_len-1:
            tags += ", "


    response = discord.Embed(title="Assessment from "+ author_name + " on " + topic_name, description=desc, color=color, url="")
    response.set_author(name=author, icon_url=author_img)
    response.set_footer(text=footer)

    response.add_field(name="Tags", value=tags)
    response.add_field(name="Attacker Value", value=data["metadata"]["attacker-value"])
    response.add_field(name="Exploitability", value=data["metadata"]["exploitability"])
    response.add_field(name="Written on", value=data["revisionDate"][:10])
    response.add_field(name="Assessment's score", value=data["score"])

    return response

def user(data):
    title = data["username"]
    url = base_url + "/contributors/"+data["username"]

    response = discord.Embed(title=title, color=color, url=url)

    response.set_image(url=data["avatar"])

    response.add_field(name="ID", value=data["id"])
    response.add_field(name="Joined on", value=data["created"][:10])
    response.add_field(name="Score", value=data["score"])

    response.set_author(name=author, icon_url=author_img)
    response.set_footer(text=footer)

    return response

def not_found(message):
    title = "Nothing found!"
    desc = message
    url = base_url

    response = discord.Embed(title=title, description=desc, color=color, url=url)
    response.set_author(name=author, icon_url=author_img)
    response.set_footer(text=footer)

    return response