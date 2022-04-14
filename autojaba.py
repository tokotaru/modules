from .. import loader

import time




class jabaMod(loader.Module):

    strings = {"name": "autojaba"}




    async def watcher(self, message):

            

        if "Тебе жаба, Милая Беседа ❤" in message.text:

            await message.client.send_message(message.chat.id, "взять жабу")