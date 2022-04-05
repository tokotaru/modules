from .. import loader, utils

class InfoMod(loader.Module):
	strings = {"name": "ChannelDel"}
	
	async def onccmd(self, message):
		await message.edit("On")
		self.truefalse = True
		self.chat = message.chat_id
		self.me = (await message.client.get_me()).id

	async def offccmd(self, message):
		await message.edit("Off")
		self.truefalse = False
		
	async def watcher(self, message):
		sender = await message.get_sender()
		if sender.id == self.me:
			return
		if self.truefalse == False:
			return
		if int(message.chat_id) != self.chat:
			return
		msg_id = message.id
		a = str(sender).split("(", maxsplit=1)[0]
		if a != "Channel":
			return
		await message.client.delete_messages(message.chat_id, msg_id)
