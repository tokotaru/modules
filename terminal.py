from .. import loader
import time
import subprocess
class AMod(loader.Module):
    strings = {"name": "терминал вроде"}

    async def watcher(self, message):
        if message.sender_id != (await message.client.get_me()).id:
            return
        if message.text == ".pip <command>":
          a=message.text.split(" ")
          bashCommand = a[1]
          process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
          output, error = process.communicate()
          await message.edit("сделано,мой повелитель,вот вывод:\n {}".format(output and error))
