import disnake
from disnake.ext import commands
from disnake.utils import get
from youtube_dl import YoutubeDL

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


class MusicCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, arg):
        try:
            vc = await ctx.message.author.voice.channel.connect()

            with YoutubeDL(YDL_OPTIONS) as ydl:
                if 'https://' in arg:
                    info = ydl.extract_info(arg, download=False)
                else:
                    info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]

            url = info['formats'][0]['url']

            vc.play(disnake.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=url, **FFMPEG_OPTIONS))
        except:
            await ctx.send(f'{ctx.author.mention} Вы не находитесь в голосовом канале')

    @commands.command(name='pause')
    async def pause(self, ctx):
        author = ctx.message.author
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            await ctx.send(f'Пользователь {author.mention} поставил текущую музыку на паузу.')

    @commands.command(pass_context=True, aliases=['resume', 'пуск'])
    async def resum(self, ctx):
        author = ctx.message.author
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        voice.resume()
        await ctx.send(f'Пользователь {author.mention} резюме трек')

    @commands.command(name='stop')
    async def stop(self, ctx):
        author = ctx.message.author

        voice = get(self.bot.voice_clients, guild=ctx.guild)
        await voice.disconnect()
        await ctx.send(f"{author.mention} выгнал бота")

def setup(bot):
    bot.add_cog(MusicCMD(bot))
