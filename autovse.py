from .. import loader		
from asyncio import sleep
from datetime import datetime
import pytz     #   pip install pytz
#модуль не готов
class autoMod(loader.Module):
    strings = {"name": "autovse"}
    def m_time():
        time = datetime.now(pytz.timezone('Europe/Moscow'))
        time=time.strftime('%H:%M:%S')
        return str(time)
    def __init__(self):
        self.farm = True
        self.virys = True
        self.feed = True
        self.work = True
        self.five = True
    async def farmcmd(self, message):
        while self.farm:
                time=await m_time()
                if time == "00:00:00" or time == "04:00:00" or time == "08:00:00" or time == "12:00:00" or time == "16:00:00" or time == "20:00:00" or time == "24:00:00":
                    await message.reply("ферма")
