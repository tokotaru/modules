from .. import loader		
from asyncio import sleep
#модуль не готов
class autoMod(loader.Module):
	strings = {"name": "autovse"}
	
	def __init__(self):
		self.farm = True
		self.virys = True
                self.feed = True
                self.work = True
		
	async def farmcmd(self, message):
		"""Включает команду "Ферма". Чтобы остановить, используйте "ирисфарм стоп"."""
		while self.farm:
			await message.reply("Ферма")
			await sleep(14500)
        async def feedcmd(self, message):
		"""Включает команду "покормить жабу". Чтобы остановить, используйте "ирисфарм стоп"."""
		while self.farm:
			await message.reply("покормить жабу")
			await sleep(14500)
