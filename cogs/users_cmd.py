import random
from typing import Optional

import discord
import disnake
from disnake.ext import commands

from parsers.analcontent import get_anime
from parsers.general_hs import get_meme
from parsers.liga_plohih_shutok import get_anek


class Confirm(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout=10.0)
        self.value = Optional[bool]

    @disnake.ui.button(label='Да', style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        self.value = True
        self.stop()

    @disnake.ui.button(label='порно', style=disnake.ButtonStyle.red, emoji='✔')
    async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        self.value = False
        self.stop()

    @disnake.ui.button(label='я подумаю', style=disnake.ButtonStyle.blurple)
    async def think(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        self.stop()


class LinkToConf(disnake.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(disnake.ui.Button(label='СылОчка', url='https://youtu.be/PPFMQ0-bfBE?t=12', style=disnake.ButtonStyle.danger))


class Dropdown(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label='тяп', description='тяп тяп тяп'),
            disnake.SelectOption(label='гренки', description='ма'),
            disnake.SelectOption(label='писсуар', description='йцу')
        ]
        super().__init__(
            placeholder="MENU",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.send_message(f'Вы выбрали {self.values[0]}')


class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


class CMDUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(1075500941215801344)
        await channel.send('Я включился')
        print('BOT READY')


    @commands.command()
    async def help(self, ctx):
        embed = disnake.Embed(title='Навигация по командам', color=disnake.Color.green())

        embed.add_field(name='!тян', value='тян')
        embed.add_field(name='!c', value='Очистка чата')
        embed.add_field(name='!play', value='Поставить свой трек с ютуба')
        embed.add_field(name='!pause', value='пуза')
        embed.add_field(name='!resume', value='врубить')
        embed.add_field(name='!вопрос', value='вопросы')
        embed.add_field(name='!order', value='меню')

        await ctx.send(embed=embed)

    @commands.command(name='тян')
    async def tyan(self, ctx):
        anime = get_anime()
        await ctx.send(anime)

    @commands.command(name='анек')
    async def anek(self, ctx):
        anek = get_anek()
        await ctx.send(anek)

    @commands.command(name='гена')
    async def gena(self, ctx):
        gena = get_meme()
        await ctx.send(gena)

    @commands.command(name='say')
    async def say(self, ctx, *, text):
        channel = self.bot.get_channel(1075500941215801344)
        await channel.send(text)

    #@commands.command(name='тарзан', aliases=['т'])
    #async def tarzan(self, ctx):
    #    meme = get_meme()
    #    if meme['text']:
    #        await ctx.send(meme['text'])
    #    await ctx.send(meme['url'])

    @commands.command()
    async def order(self, ctx):
        await ctx.send('Выберите что-нибудь', view=DropdownView())

    @commands.command(name='вопрос')
    async def ques(self, ctx):
        view = Confirm()
        link = LinkToConf()

        await ctx.send('Вы тарзан?', view=view)
        await view.wait()

        if view.value is None:
            await ctx.send('Время вышло')
        elif view.value:
            await ctx.send('круто', view=link)
        else:
            await ctx.send('порно')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        embed = disnake.Embed(title=f'Leathermans поздоровайтесь! Новый Slave в нашем Gym',
                              description=f'Когда он родился, сам Dungeon Master прокричал - AAAAAAHHH YEEAAH'
                                          f'\n{member.mention} Здесь ты раскроешь не только себя и то кто ты есть, но и свой anal',
                              color=0x1E90FF)
        await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author != self.bot.user:
            with open('danger_words.txt', 'r', encoding='utf-8') as file:
                d_words = file.read()

            a = random.randint(1, 100)
            if 1 == a and message.author.id != 365835967657148417:
                try:
                    await message.channel.send(f'{message.author.mention} опа, не фортануло дружочек')
                    await message.author.send(f'На\nhttps://discord.gg/exB5jdBw')
                    await message.author.kick(reason='Нарушение правил')
                except:
                    print('у меня нет прав')
                    await message.channel.send(
                        f'{message.author.mention} Кикнуть тебя я не могу, так что считай тебя кикнули сынок')

            for mes in message.content.split():
                if mes in d_words.split('\n'):
                    await message.channel.send(f'{message.author.mention} мать у тебя {mes} понял?')

                if message.channel.id == 1075500961407176844 and message.content[0] != '!':
                    await message.channel.send(f'{message.author.mention} ЭЭЭ бля, это моя территория нефор, ты че из этих? пауков?')
                    await message.delete()


def setup(bot):
    bot.add_cog(CMDUsers(bot))