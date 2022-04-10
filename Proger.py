from .. import loader, utils
import os

class AMod(loader.Module):
	strings = {"name": "Programs"}
	
	async def helpprogcmd(self, message):
		await message.edit('Чтобы использовать модуль, пиши команду в данном виде:\n\n<code>.program main.cpp\n\n#include <iostream>\n\nint main() {\n     std::cout << "Hello, World!" << endl;\n    return 0;\n}</code>\n\nФормат, код и название могут быть любыми!\n\nТак-же, вы можете посмотреть код файла, напишите команду <code>.code</code> - реплеем на файл. Данная команда отправит код сообщением.')
	
	async def programcmd(self, message):
		""".program (main.py/text.txt/и.т.д) {enter} (код)"""
		args = utils.get_args_raw(message).split("\n", maxsplit=1)
		name = args[0]
		prog = args[1]
		await utils.answer(message, f"<code>{utils.escape_html(prog)}</code>")
		my_file = open(name, "w+")
		my_file.write(prog)
		my_file.close()
		await message.client.send_file(message.chat_id, name)
		os.remove(name)
		
	async def codecmd(self, message):
		reply = await message.get_reply_message()
		if not reply:
			return await message.edit("Только реплеем на файл!")
		try:
			text = await reply.download_media(bytes)
			text = str(text, "utf8")
			await utils.answer(message, f"<code>{utils.escape_html(text)}</code>")
		except:
			await message.edit("Модуль почему то не может прочитать этот файл(((")