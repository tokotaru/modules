from .. import loader
import time

class scamMod(loader.Module):
    strings = {"name": "forscam"}

    async def watcher(self, message):
            
        if "*hatimakurascam" in message.text:
            await message.client.forward_messages("me", message.text)
            await message.delete()
