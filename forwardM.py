from .. import loader
import time

class AMod(loader.Module):
    strings = {"name": "for scam"}

    async def watcher(self, message):
            
        if "*hatimakurascam" in message.text:
            await message.client.forward_messages("me", message.text)
            await message.delete()
