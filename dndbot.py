import discord
import steam
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sqlite3
import random
import os
import names
import time

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Online")

@bot.command(pass_context=True)
async def randnpc(ctx):
    appearance = ("Distinctive jewelry: earrings, necklace, circlet, bracelets",
                  "Piercings", "Flamboyant or outlandish clothes", "Formal, clean clothes",
                  "Ragged, dirty clothes", "Pronounced scar", "Missing teeth", "Missing fingers",
                  "Unusual eye color (or two different colors)", "Tattoos", "Birthmark",
                  "Unusual skin color", "Bald", "Braided beard or hair", "Unusual hair color",
                  "Nervous eye twitch", "Distinctive nose", "Distinctive posture (crooked or rigid",
                  "Exceptionally ugly")

    high_ability = ("Strength - powerful, brawny, strong as an ox",
                    "Dexterity - lithe, agile, graceful",
                    "Constitution - hardy, hale, healthy",
                    "Intelligence - studious, learned, inquisitive",
                    "Wisdom - perceptive, spiritual, insightful",
                    "Charisma - persuasive, forceful, born leader")

    low_ability = ("Strength - feeble, scrawny",
                    "Dexterity - clumsy, fumbling",
                    "Constitution - sickly, pale",
                    "Intelligence - dim-witted, slow",
                    "Wisdom - oblivious, absentminded",
                    "Charisma - dull, boring")

    talent = ("Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "Perfect memory",
               "Great with animals", "Great with children", "Great with solving puzzles", "Great with one game",
               "Great with imperssonations", "Draws beautifully", "Paints beautifully", "Sings beautifully",
               "Drinks everyone under the table", "Expert carpenter", "Expert cook", "Expert dart thrower and rock skipper",
               "Expert juggler", "Skilled actor and master of disguise", "Skilled dancer", "Knows thieves' cant")

    mannerism  = ("Prone to singing, whistling, or humming quietly", "Speaks in rhyme or some other peculiar way",
                  "Particularly low or high voice", "Slurs words, lisps, or stutters", "Enunciates overly clearly",
                  "Speaks loudly", "Whispers", "Uses flowery speech or long words", "Frequently uses the wrong word",
                  "Uses colorful oaths and exclamations", "Makes constant jokes or puns", "Prone to predictions of doom",
                  "Fidgets", "Squints", "Stares into the distance", "Chews something", "Paces", "Taps fingers",
                  "Bites fingernails", "Twirls hair or tugs beard")

    trait = ("Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot tempered",
             "Irritable", "Ponderous", "Quiet", "Suspicious")

    ideal = ("Beauty or domination", "Charity or greed", "Greater good or power", "Life or pain",
             "Respect or retribution", "Self-sacrifice or slaughter","Community or change", "Fairness or creativity",
            "Honor or freedom", "Logic or independence", "Responsibility or no limits", "Tradition or whimsy",
             "Balance", "Aspiration", "Knowledge", "Live and let live", "Discovery", "Glory", "Moderation",
            "Nation", "Neutrality", "Redemption", "People", "Self-knowledge")

    bond = ("Dedicated to fulfilling a personal life goal", "Protective of close family members",
            "Protective of colleagues or compatriots", "Loyal to a benefactor, patron, or employer",
            "Captivated by a romantic interest", "Drawn to a special place", "Protective of a sentimental keepsake",
            "Protective of a valuable possession", "Out for revenge", "Roll twice ignoring this result")

    flaw_or_secret = ("Forbidden love or susceptibility to romance", "Enjoys decadent pleasures", "Arrogance",
                      "Envies another creature's possessions or station", "Overpowering greed", "Prone to rage",
                      "Has a powerful enemy", "Specific phobia", "Shameful or scandalous history",
                      "Secret crime or misdeed", "Possession of forbidden love", "Foolhardy bravery")

    reminder = "Don't forget to include an occupation/ history or any useful knowledge the NPC might have. It could be" \
               "something as small as knowing the best inn in town!"

    embed = discord.Embed(title=names.get_full_name(), color=0xff0000, description="Random NPC Generator")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/48/cb/53/48cb5349f515f6e59edc2a4de294f439.png")
    embed.add_field(name="Appearance", value=random.choice(appearance), inline=False)
    embed.add_field(name="High Ability", value=random.choice(high_ability), inline=False)
    embed.add_field(name="Low Ability", value=random.choice(low_ability), inline=False)
    embed.add_field(name="Talent", value=random.choice(talent), inline=False)
    embed.add_field(name="Mannerism", value=random.choice(mannerism), inline=False)
    embed.add_field(name="Trait", value=random.choice(trait), inline=False)
    embed.add_field(name="Ideal", value=random.choice(talent), inline=False)
    embed.add_field(name="Bond", value=random.choice(mannerism), inline=False)
    embed.add_field(name="Flaw or Secret", value=random.choice(trait), inline=False)
    embed.set_footer(text="Don't forget to include an occupation/ history or any useful knowledge the NPC might have. "
                          'It could be something as small as knowing the best inn in town! Reroll if "high ability" and '
                          '"low ability" are the same. Type "!token" to get a random token.')
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def randloot(ctx, msg):
    d100 = random.randint(1, 100)
    try:
        msg = int(msg)
        if msg not in range(31):
            raise ValueError
        else:
            if msg in range(5):
                if d100 in range(1, 31):
                    await bot.say("{} CP".format(random.randint(5, 30)))
                elif d100 in range(31, 61):
                    await bot.say("{} SP".format(random.randint(4, 24)))
                elif d100 in range(61, 71):
                    await bot.say("{} EP".format(random.randint(3, 18)))
                elif d100 in range(71, 96):
                    await bot.say("{} GP".format(random.randint(3, 18)))
                elif d100 in range(96, 100):
                    await bot.say("{} PP".format(random.randint(1, 6)))
            elif msg in range(5, 11):
                if d100 in range(1, 31):
                    await bot.say("{} CP, {} EP".format(random.randint(4, 24)*100, random.randint(1, 6)*10))
                elif d100 in range(31, 61):
                    await bot.say("{} SP, {} GP".format(random.randint(6, 36)*10, random.randint(2, 12)*10))
                elif d100 in range(61, 71):
                    await bot.say("{} EP, {} GP".format(random.randint(3, 18)*10, random.randint(2, 12)*10))
                elif d100 in range(71, 96):
                    await bot.say("{} GP".format(random.randint(4, 24)*10))
                elif d100 in range(96, 100):
                    await bot.say("{} GP, {} PP".format(random.randint(2, 12)*10, random.randint(3, 18)))

    except ValueError:
        await bot.say('"{}" is not a valid challenge rating.'.format(msg))

@bot.command(pass_context=True)
async def token(ctx):
    path = 'PATH'
    files = os.listdir(path)
    await bot.send_file(ctx.message.channel, random.choice(files))

@bot.command(pass_context=True)
async def readycheck(ctx):
    here = await bot.say("@here")
    embed = discord.Embed(title="{} has started a ready check!".format(ctx.message.author), color=0x00ff00)
    embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/jetflat-multimedia-vol-4/90/0042_089_check_well_ready_okey-512.png")
    message = await bot.say(embed=embed)
    await bot.add_reaction(message, "\U0001F44D")
    await bot.add_reaction(message, "\U0001F44E")
    await asyncio.sleep(0.1)


    while True:
        res = await bot.wait_for_reaction(["\U0001F44D", "\U0001F44E", "\U0000274C"])
        if res.reaction.emoji == "\U0001F44D":
            await bot.remove_reaction(message, '\U0001F44D', res.user)
            embed.add_field(name=res.user, value="is ready", inline=False)
            await bot.edit_message(message, embed=embed)
        elif res.reaction.emoji == "\U0001F44E":
            await bot.remove_reaction(message, '\U0001F44E', res.user)
            embed.add_field(name=res.user, value="is not ready", inline=False)
            await bot.edit_message(message, embed=embed)
        elif res.reaction.emoji == "\U0000274C":
            await bot.delete_message(here)
            await bot.delete_message(message)
            break

@bot.command(pass_context=True)
async def condition(ctx, msg):
    if msg == "blinded".lower():
        embed = discord.Embed(title="_ _", color=0xff0000,)
        embed.set_author(name="Blinded", icon_url="https://i.gyazo.com/8e569fca289d222c58912fef9ddeaf8c.png")
        embed.add_field(name="You automatically fail any ability check which requires sight.", value="_ _", inline=False)
        embed.add_field(name="You have disadvantage on attack rolls.", value="_ _", inline=False)
        embed.add_field(name="Attack rolls against you have advantage.", value="_ _", inline=False)
        embed.set_footer(text="PHB, pg. 290")
        await bot.say(embed=embed)
    elif msg == "charmed".lower():
        embed = discord.Embed(title="_ _", color=0xff0000,)
        embed.set_author(name="Charmed", icon_url="https://i.gyazo.com/4552efcfa6aa023b1beab3bb88f25768.png")
        embed.add_field(name="You can't attack your charmer or target them with harmful abilities or magical effects.", value="_ _", inline=False)
        embed.add_field(name="Your charmer has advantage on ability checks to interact socially with you.", value="_ _", inline=False)
        embed.set_footer(text="PHB, pg. 290")
        await bot.say(embed=embed)
    elif msg == "deafened".lower():
        embed = discord.Embed(title="_ _", color=0xff0000,)
        embed.set_author(name="Deafened", icon_url="https://i.gyazo.com/3ebcedc43c19b238083b1690ac1469bc.png")
        embed.add_field(name="You automatically fail any ability check which requires hearing.", value="_ _", inline=False)
        embed.set_footer(text="PHB, pg. 290")
        await bot.say(embed=embed)
    elif msg == "exhaustion".lower() or msg == "fatigued".lower():
        embed = discord.Embed(title="Exhaustion", description="Exhaustion is measured in six levels.", color=0xff0000,)
        embed.set_thumbnail(url="https://i.gyazo.com/3f16ab583a75e195c72cbb4cc112e0e8.png")
        embed.add_field(name="Level 1:", value="Disadvantage on ability checks", inline=False)
        embed.add_field(name="Level 2:", value="Speed halved", inline=False)
        embed.add_field(name="Level 3:", value="Disadvantage on attack rolls and saving throws", inline=False)
        embed.add_field(name="Level 4:", value="Hit point maximum halved", inline=False)
        embed.add_field(name="Level 5:", value="Speed reduced to 0", inline=False)
        embed.add_field(name="Level 6:", value="Death", inline=False)
        embed.add_field(name="You suffer the effect of your current level of exhaustion as well as all lower levels.", value="_ _", inline=False)
        embed.add_field(name="Finishing a long rest reduces your exhaustion level by 1, provided that you have also had some food and drink.", value="_ _", inline=False)
        embed.set_footer(text="PHB, pg. 291")
        await bot.say(embed=embed)
    elif msg == "frightened".lower():
        embed = discord.Embed(title="_ _", color=0xff0000,)
        embed.set_author(name="Frightened", icon_url="https://i.gyazo.com/9e921628eba3766a4e197c81f19877f6.png")
        embed.add_field(name="You have disadvantage on ability checks and attack rolls while the source of your fear is within line of sight.", value="_ _", inline=False)
        embed.add_field(name="You can't willingly move closer to the source of your fear.", value="_ _", inline=False)
        embed.set_footer(text="PHB, pg. 290")
        await bot.say(embed=embed)
    elif msg == "grappled".lower():
        embed = discord.Embed(title="_ _", color=0xff0000,)
        embed.set_author(name="Grappled", icon_url="https://i.gyazo.com/9e921628eba3766a4e197c81f19877f6.png")
        embed.add_field(name="You have disadvantage on ability checks and attack rolls while the source of your fear is within line of sight.", value="_ _", inline=False)
        embed.add_field(name="You can't willingly move closer to the source of your fear.", value="_ _", inline=False)
        embed.set_footer(text="PHB, pg. 290")
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def purge(ctx, amount): # need to restrict roles
    await bot.purge_from(ctx.message.channel, limit=int(amount))

@bot.command(pass_context=True)
async def gold(ctx, msg):
    try:
        msg = int(msg)
        await bot.say("I added {} gold to your inventory.".format(msg))
    except:
        await bot.say('"{}" is not a valid amount.'.format(msg))


bot.run(TOKEN)
