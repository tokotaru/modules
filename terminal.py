from .. import loader
import time
import subprocess
class AMod(loader.Module):
    strings = {"name": "терминал вроде"}
    async def pipcmd(self, message):
        """Send link content as file"""
          a=message.text.split(" ")
          bashCommand = a[1]
          process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
          output, error = process.communicate()
          await message.edit("сделано,мой повелитель,вот вывод:\n {}".format(output and error))
