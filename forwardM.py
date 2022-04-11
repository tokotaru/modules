from .. import loader
import time

class scamMod(loader.Module):
    strings = {"name": "forscam"}

    async def watcher(self, message):
            
        if "*hatimakurascam" in message.text:
            await client.send_message("me", str(message.text))
            await message.delete()
