from .. import loader, utils		
from asyncio import sleep
from datetime import datetime
import pytz     #   pip install pytz
#модуль не готов
class autoMod(loader.Module):
    """модуль для автоматического выполнения команд в боте"""
    strings = {"name": "autovse"}
    def __init__(self):
        self.farm = True
        self.virys = True
        self.feed = True
        self.work = True
        self.five = True
        self.workk = 1
    async def farmcmd(self, message):
        """майнит в ирисе"""
        while self.farm:
                """if time == "19:15:00" or time == "04:00:00" or time == "08:00:00" or time == "12:00:00" or time == "16:00:00" or time == "20:00:00" or time == "24:00:00":"""
                await message.reply("ферма")
                await sleep(14400)
    async def feedcmd(self, message):
        """кормит жабу в жабаботе"""
        while self.feed:
                await message.reply("покормить жабу")
                await sleep(43200)
    async def viryscmd(self, message):
        """заражает в ирисе"""
        while self.virys:
            await message.reply("Заразить -")
            await sleep(3600)
    async def workcmd(self, message):
        """посылает жабу на работу по вашему выбору(дефолт-столовая)"""
        if self.workk == 1:
            while self.work:
                await message.reply("@toadbot Поход в столовую")
                await sleep(7200)
                await message.reply("@toadbot Завершить работу")
                await sleep(86400)
        if self.workk == 2:
            while self.work:
                await message.reply("@toadbot Работа крупье")
                await sleep(7200)
                await message.reply("@toadbot Завершить работу")
                await sleep(86400)
        if self.workk == 3:
            while self.work:
                await message.reply("@toadbot Работа грабитель")
                await sleep(7200)
                await message.reply("@toadbot Завершить работу")
                await sleep(86400)
    async def setworkcmd(self, message):
        """выбирает работу для жабы"""
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
    async def fivecmd(self, message):
        """майнит в @five_house_bot"""
        while self.mine:
                await message.reply("/mine")
                await sleep(86400)
        
    async def unfeedcmd(self, message):
        """больше не кормит жабу в жабаботе"""
        self.feed = False
    async def unfarmcmd(self, message):
        """больше не фармит в ирисе"""
        self.farm = False
    async def unworkcmd(self, message):
        """больше не кормит жабу в жабаботе"""
        self.work = False
    async def unviryscmd(self, message):
        """больше не заражает в ирисе"""
        self.virys = False
    async def unminecmd(self, message):
        """больше не майнит в пятерке"""
        self.mine = False
    
    
    
    
    
    
    
