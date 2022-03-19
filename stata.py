from .. import loader 
from telethon.tl.types import * 
class stataMod(loader.Module): 
    "покажет статистику чата за всё время\n\n\nВ лс не работает!!!" 
    strings = {"name": "StataChat"} 
    async def statacmd(self, m):
        chatid = str(m.chat_id) 
        chat = await m.client.get_entity(int(chatid))
        al = str((await m.client.get_messages(m.to_id, limit=0)).total) 
        ph = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterPhotos())).total) 
        vi = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total) 
        mu = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterMusic())).total) 
        vo = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVoice())).total) 
        vv = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterRoundVideo())).total) 
        do = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterDocument())).total) 
        urls = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterUrl())).total) 
        gifs = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGif())).total) 
        cont = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterContacts())).total)
        await m.respond(
            ( "<b>Информация о чате:</b> {}\n\n" 
            "<b>количество сообщений:</b> {}\n" 
             "<b>количество фото:</b> {}\n" 
             "<b>количество видео:</b> {}\n" 
             "<b>количество музыки:</b> {}\n" 
             "<b>количество голосовых:</b> {}\n" 
             "<b>количество видеосообщний:</b> {}\n" 
             "<b>количество файлов:</b> {}\n" 
             "<b>количество ссылок:</b> {}\n" 
             "<b>количество гивок:</b> {}\n" 
             "<b>количество номеров:</b> {}").format(chat.title, al, ph, vi, mu, vo, vv, do, urls, gifs, cont))
