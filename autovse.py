from .. import loader		
from asyncio import sleep
from datetime import datetime
import pytz     #   pip install pytz
#модуль не готов
class autoMod(loader.Module):
	strings = {"name": "autovse"}
	def m_time():
            time = datetime.now(pytz.timezone('Europe/Moscow'))
            time=time.strftime('%H:%M')
            return str(time)
	def __init__(self):
            self.farm = True
            self.virys = True
            self.feed = True
            self.work = True
            self.five = True
	async def farmcmd(self, message):
		"""Включает команду "Ферма". Чтобы остановить, используйте "ирисфарм стоп"."""
            while self.farm:
                    if m_time() == "00:00" or m_time() == "04:00" or m_time() == "08:00" or m_time() == "12:00" or m_time() == "16:00" or m_time() == "20:00" or m_time() == "24:00":
                        await message.reply("Ферма")
        """async def feedcmd(self, message):
		"""Включает команду "покормить жабу". Чтобы остановить, используйте "ирисфарм стоп"."""
		while self.farm:
			await message.reply("покормить жабу")
			await sleep(14500)"""
        async def watcher(self, message):
            me = (await message.client.get_me())
            if message.sender_id == me.id:
                if message.text.lower() == "ирисфарм стоп":
                    self.farm = False
                    await message.reply("<b>Ирисфарм остановлен.</b>")
                if message.text.lower() == "ирисвирус стоп":
                    self.virys = False
                    await message.reply("<b>Ирисвирус остановлен.</b>")
