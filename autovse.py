from .. import loader, utils		
from asyncio import sleep
from datetime import datetime
import pytz     #   pip install pytz
#модуль не готов
class autoMod(loader.Module):
    strings = {"name": "autovse"}
    def m_time():
        time = datetime.now(pytz.timezone('Europe/Moscow'))
        time=time.strftime('%H:%M:%S')
    def __init__(self):
        self.farm = True
        self.virys = True
        self.feed = True
        self.work = True
        self.five = True
        self.workk = 1
    async def farmcmd(self, message):
        while self.farm:
                """if time == "19:15:00" or time == "04:00:00" or time == "08:00:00" or time == "12:00:00" or time == "16:00:00" or time == "20:00:00" or time == "24:00:00":"""
                await message.reply("ферма")
                sleep(14400)
    async def feedcmd(self, message):
        while self.feed:
                await message.reply("покормить жабу")
                sleep(43200)
    async def viryscmd(self, message):
        while self.virys:
            await message.reply("Заразить -")
            await sleep(3600)
    async def setworkcmd(self, message):
        work = utils.get_args_raw(message)
        if work == "1" or work == "2" or work == "3":
            if work == "1":
                self.workk = 1
                await message.reply("работа поход в столовую поставленна")
            if work == "2":
                self.workk = 2
                await message.reply("работа крупье поставленна")
            if work == "3":
                self.workk = 3
                await message.reply("работа грабитель поставленна")
        else:
            await message.reply("не правильные аргументы,введите 1,2 или 3")
        
    
