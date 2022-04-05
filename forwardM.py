from .. import loader
import time

class AMod(loader.Module):
    strings = {"name": "пересылатель в избранные"}

    async def watcher(self, message):
        if message.sender_id != (await message.client.get_me()).id:
            return
        if message.text == "#+":
            await message.client.forward_messages("me", (await message.get_reply_message()))
            await message.edit("сделано,мой повелитель")
            time.sleep(3)
            await message.delete()