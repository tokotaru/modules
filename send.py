from .. import loader
import time
class jabaMod(loader.Module):
    strings = {"name": "autojaba"}




    async def watcher(self, message):

            

        if "vsend" in message.text:
            a=message.text.split(" ")
            a=str(a[1])
            await message.client.send_message(message.chat.id, a)
