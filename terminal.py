from .. import loader
import time
import subprocess
class AMod(loader.Module):
    strings = {"name": "терминал вроде"}

    async def watcher(self, message):
        if message.sender_id != (await message.client.get_me()).id:
            return
        if ".pip" in message.text:
            a=message.text.split(" ")
            bashCommand = "pip3 install"+a[1]
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            await message.edit("сделано,мой повелитель,вот вывод:\n {}".format(output))
