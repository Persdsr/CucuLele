import disnake
from disnake.ext import commands


class ModerCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def c(self, ctx, amount=0):
        if amount == 0:
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban_word(self, ctx, word):
        with open('danger_words.txt', 'a', encoding='utf-8') as file:
            file.write(f'{word}\n\n')

    @commands.command()
    @commands.has_permissions()
    async def kick(self, ctx, member: disnake.Member, *, reason='Нарушение правил'):
        await member.kick(reason=reason)

def setup(bot):
    bot.add_cog(ModerCMD(bot))