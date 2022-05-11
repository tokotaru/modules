from .. import loader
import time
class sendMod(loader.Module):
    strings = {"name": "send"}
    #a



    async def watcher(self, message):

            

        if "vsend" in message.text:
            a=message.text.split(" ", 1)
            a=str(a[1])
            await message.client.send_message(message.chat.id, a)
