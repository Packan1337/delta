import discord
import aiohttp, io
from discord.ext import commands
import praw, random
from config import bot_color2, reddit_id, reddit_secret, img_fail

class meme_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    # Post memes from reddit
    @discord.slash_command(name="meme", description="Post memes from reddit")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("subreddit", description="Choose a subreddit", choices=["r/memes", "r/dankmemes", "r/shitposting", "r/me_irl", "r/ProgrammerHumor", "r/softwaregore", "r/furrymemes"], required=True)
    async def meme(self, ctx: discord.ApplicationContext, subreddit: str):
        await ctx.defer()
        reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent='Delta', check_for_async=False)
        post_to_pick = random.randint(1, 50)

        if subreddit == "r/memes":
            memes_submissions = reddit.subreddit('memes').hot()
        elif subreddit == "r/dankmemes":
            memes_submissions = reddit.subreddit('dankmemes').hot()
        elif subreddit == "r/shitposting":
            memes_submissions = reddit.subreddit('shitposting').hot()
        elif subreddit == "r/me_irl":
            memes_submissions = reddit.subreddit('me_irl').hot()
        elif subreddit == "r/ProgrammerHumor":
            memes_submissions = reddit.subreddit('ProgrammerHumor').hot()
        elif subreddit == "r/softwaregore":
            memes_submissions = reddit.subreddit('softwaregore').hot()
        elif subreddit == "r/furrymemes":
            memes_submissions = reddit.subreddit('furrymemes').hot()

        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embed = discord.Embed(color=bot_color2, title=submission.title)
        embed.set_image(url=submission.url)
        await ctx.followup.send(embed=embed)

    
    memegen = discord.SlashCommandGroup("memegen", "Create memes") # Create memes
    usermemegen = memegen.create_subgroup("user", "Create memes with others")

    # One panel memes
    @memegen.command(name="--onepanel", description="Make memes")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("template", str, description="Choose a template", choices=["oogway", "pikachu", "biden", "facts", "sad cat", "iphone alert", "caution", "change my mind", "lisa", "worthless", "burn"], required=True)
    @discord.option("title", str, description="An interesting title", required=True)
    @discord.option("text", str, description="Meme text", required=True)
    async def memegen_onepanel(self, ctx, template: str, title: str, text: str):
        await ctx.defer()
        #global api

        if template == "oogway":
            api = "https://api.popcat.xyz/oogway"
        elif template == "pikachu":
            api = "https://api.popcat.xyz/pikachu"
        elif template == "biden":
            api = "https://api.popcat.xyz/biden"
        elif template == "facts":
            api = "https://api.popcat.xyz/facts"
        elif template == "sad cat":
            api = "https://api.popcat.xyz/sadcat"
        elif template == "iphone alert":
            api = "https://api.popcat.xyz/alert"
        elif template == "caution":
            api = "https://api.popcat.xyz/caution"

        elif template == "change my mind":
            api = "https://frenchnoodles.xyz/api/endpoints/changemymind"
        elif template == "lisa":
            api = "https://frenchnoodles.xyz/api/endpoints/lisastage"
        elif template == "worthless":
            api = "https://frenchnoodles.xyz/api/endpoints/worthless"
        elif template == "burn":
            api = "https://frenchnoodles.xyz/api/endpoints/spongebobburnpaper"

        meme_text = text.replace(" ", "+")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}?text={meme_text}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme.png")
                    
                    embed = discord.Embed(color=bot_color2, title=title)
                    embed.set_image(url="attachment://meme.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # Two panel memes
    @memegen.command(name="--twopanel", description="Make better memes")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("template", str, description="Choose a template", choices=["drake", "pooh", "npc"], required=True)
    @discord.option("title", str, description="A very interesting title", required=True)
    @discord.option("text1", str, description="Top panel text", required=True)
    @discord.option("text2", str, description="Bottom panel text", required=True)
    async def usermemegen_twopanel(self, ctx, template: str, title: str, text1: str, text2:str):
        await ctx.defer()

        if template == "drake":
            api = "https://api.popcat.xyz/drake"
        elif template == "pooh":
            api = "https://api.popcat.xyz/pooh"
        elif template == "npc":
            api = "https://vacefron.nl/api/npc"

        panel1 = text1.replace(" ", "+")
        panel2 = text2.replace(" ", "+")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}?text1={panel1}&text2={panel2}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme2.png")
                    
                    embed = discord.Embed(color=bot_color2, title=title)
                    embed.set_image(url="attachment://meme2.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # User memes
    @usermemegen.command(name="--twouser", description="Crate memes with someone")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("template", str, description="Choose a template", choices=["confused cat", "milk"], required=True)
    @discord.option("title", str, description="Post title", required=True)
    @discord.option("user1", discord.Member, description="Select a user", required=True)
    @discord.option("user2", discord.Member, description="and an another one", required=True)
    async def memegen_twouser(self, ctx, template: str, title: str, user1: discord.Member, user2: discord.Member):
        await ctx.defer()
        global url
        avatar1 = user1.avatar
        avatar2 = user2.avatar

        if template == "confused cat":
            url = f"https://vacefron.nl/api/womanyellingatcat?woman={avatar1}&cat={avatar2}"
        elif template == "milk":
            url = f"https://vacefron.nl/api/icanmilkyou?user1={avatar1}&user2={avatar2}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme3.png")
                    
                    embed = discord.Embed(color=bot_color2, title=title)
                    embed.set_image(url="attachment://meme3.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()

                
    # User memes
    @usermemegen.command(name="--oneuser", description="man im dead 💀")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("template", str, description="Choose a template", choices=["adios", "first time", "drip", "clown", "horny license", "jail"], required=True)
    @discord.option("title", str, description="An interesting title", required=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    async def memegen_user(self, ctx, template: str, title: str, user: discord.Member):
        await ctx.defer()
        avatar = user.avatar

        if template == "adios":
            url = f"https://vacefron.nl/api/adios?user={avatar}"
        elif template == "first time":
            url = f"https://vacefron.nl/api/firsttime?user={avatar}"
        elif template == "drip":
            url = f"https://vacefron.nl/api/drip?user={avatar}"
            
        elif template == "clown":
            url = f"https://api.popcat.xyz/clown?image={avatar}"
            
        elif template == "horny license":
            url = f"https://some-random-api.ml/canvas/horny?avatar={avatar}"
        elif template == "jail":
            url = f"https://some-random-api.ml/canvas/jail?avatar={avatar}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme4.png")
                    
                    embed = discord.Embed(color=bot_color2, title=title)
                    embed.set_image(url="attachment://meme4.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()




def setup(bot):
    bot.add_cog(meme_cmds(bot))