import discord
from discord.ext import commands
from meme import GetMeme,SearchEmoji,generateUwU,bunny,GetCow
import time
import random
from animals import Animals

#config
token = "NzI1OTUzMDgxODExOTI3MDUx.XvocQQ.uT_XUpoqUJ0w3Kcsnb_yeaBp2-k"
prefix = '~'

print ("starting")

bot = commands.Bot(command_prefix = prefix)#set prefix



@bot.event
async def on_ready():
    print ("Ready to be MEME.")
# Prints when the bot is ready to be used.

try:
    #meme Command 
    @bot.command(brief='Create memes on the fly', description='The format is ~meme "template name" "top text" "bottom text"')
    async def meme(ctx,*args):

        await ctx.message.delete()
        try:
            link = GetMeme(*args)
            await ctx.send(link)
        except:
            await ctx.send("template not found :(")
            

    #random lmgtfy implementation cause why not
    @bot.command(brief='Do a google search for people who are too lazy do it themselves', description='The format is ~search whatever you want to search')
    async def search(ctx,*args):
        await ctx.message.delete()
        link = "https://lmgtfy.com/?q="
        x = args
        for i in range(len(x)):
            if i == 0:
                link = link + x[i]
            else:
                link = link + '+' + x[i]

        
        await ctx.send(link)

    #emoji command
    @bot.command(brief='get cute kaomojis based on how you feel', description='THe format is ~emoji emotion (put int in " " if there are multiple lines)')
    async def emoji(ctx,emoji):
        await ctx.message.delete()
        x = SearchEmoji(emoji)
        
        await ctx.send(x)

    #animal command
    @bot.command(brief='get cute animal pictures', description='The format is ~animal "animal name"')
    async def animal(ctx,name):
        await ctx.message.delete()
        animal = Animals(name)
        try:
            await ctx.send(animal.image())
        except:
            await ctx.send("we dont have that animal :(")

    #spread command
    @bot.command(brief='s p r e a d y o u r t e x t', description='The format is ~spread your entire sentence')
    async def spread(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            for j in i:
                text = text + " " + j
        
        await ctx.send(text)

    #cap command
    @bot.command(brief='rAnDoMLY CaPItAlIzAtIon', description='The format is ~cap your entire sentence')
    async def caps(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        final = ''
        for i in x:
            text = text+ " " +i

        for i in text:
            if random.randrange(0,2) == 0:
                final = final + i.upper()
            else:
                final = final + i.lower()
        
        await ctx.send(final)

    #uwu command
    @bot.command(brief='uwuify your sentences you fucking degenerate', description='The format is ~uwu whatever you want to say you furry fuck')
    async def uwu(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            text = text+ " " +i

        final = generateUwU(text)
        
        await ctx.send(final)

    #sign command
    @bot.command(brief='gets a bunny who feels strongly about what you want to say', description='The format is ~sign whatever you want to say')
    async def sign(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            text = text+ " " +i
        text = text[1:]
        final = bunny(text)
        fuck = "```" + final +"```"
        await ctx.send(fuck)


    #cow command
    @bot.command(brief='MOO', description='The format is ~cow whatever you want the cow to say')
    async def cow(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        for i in x:
            text = text+ " " +i
        shit = "```"
        final = GetCow(text)
        
        fuck = shit + str(final) + shit 
        await ctx.send(fuck)
     

    #B command
    @bot.command(brief='B', description='The format is ~b your enitire sentence')
    async def b(ctx,*args):
        await ctx.message.delete()
        x = args
        text = ''
        final = ''
        for i in x:
            text = text+ " " +i
        for i in text:
            if i == "b" or i == "B":
                final = final+":b:"
            else:
                final = final + i

        await ctx.send(final)

    #ping command
    @bot.command(brief='ping', description='The format is ~ping')
    async def ping(ctx):
        await ctx.message.delete()
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (((time.monotonic() - before))/2) * 1000
        await message.edit(content=f"Pong! :ping_pong: `{int(ping)}ms`")

except:
    pass

bot.run(token, bot=True)
# Starts the bot by passing it a token and telling it it isn't really a bot.
