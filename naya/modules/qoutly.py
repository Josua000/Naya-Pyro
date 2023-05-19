from io import BytesIO

from kynaylibs.nan.utils import *
from kynaylibs.nan.utils.http import *
from pyrogram import Client, filters
from pyrogram.types import Message

from naya import *


class QuotlyException(Exception):
    pass


async def get_message_sender_id(message: Message):
    if message.forward_date:
        if message.forward_sender_name:
            return 1
        elif message.forward_from:
            return message.forward_from.id
        elif message.forward_from_chat:
            return message.forward_from_chat.id
        else:
            return 1
    elif message.from_user:
        return message.from_user.id
    elif message.sender_chat:
        return message.sender_chat.id
    else:
        return 1


async def get_message_sender_name(message: Message):
    if message.forward_date:
        if message.forward_sender_name:
            return message.forward_sender_name
        elif message.forward_from:
            return (
                f"{message.forward_from.first_name} {message.forward_from.last_name}"
                if message.forward_from.last_name
                else message.forward_from.first_name
            )

        elif message.forward_from_chat:
            return message.forward_from_chat.title
        else:
            return ""
    elif message.from_user:
        if message.from_user.last_name:
            return f"{message.from_user.first_name} {message.from_user.last_name}"
        else:
            return message.from_user.first_name
    elif message.sender_chat:
        return message.sender_chat.title
    else:
        return ""


async def get_custom_emoji(message: Message):
    if message.forward_date:
        return (
            ""
            if message.forward_sender_name
            or not message.forward_from
            and message.forward_from_chat
            or not message.forward_from
            else message.forward_from.emoji_status.custom_emoji_id
        )

    return message.from_user.emoji_status.custom_emoji_id if message.from_user else ""


async def get_message_sender_username(message: Message):
    if message.forward_date:
        if (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            and message.forward_from_chat.username
        ):
            return message.forward_from_chat.username
        elif (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            or message.forward_sender_name
            or not message.forward_from
        ):
            return ""
        else:
            return message.forward_from.username or ""
    elif message.from_user and message.from_user.username:
        return message.from_user.username
    elif (
        message.from_user
        or message.sender_chat
        and not message.sender_chat.username
        or not message.sender_chat
    ):
        return ""
    else:
        return message.sender_chat.username


async def get_message_sender_photo(message: Message):
    if message.forward_date:
        if (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            and message.forward_from_chat.photo
        ):
            return {
                "small_file_id": message.forward_from_chat.photo.small_file_id,
                "small_photo_unique_id": message.forward_from_chat.photo.small_photo_unique_id,
                "big_file_id": message.forward_from_chat.photo.big_file_id,
                "big_photo_unique_id": message.forward_from_chat.photo.big_photo_unique_id,
            }
        elif (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            or message.forward_sender_name
            or not message.forward_from
        ):
            return ""
        else:
            return (
                {
                    "small_file_id": message.forward_from.photo.small_file_id,
                    "small_photo_unique_id": message.forward_from.photo.small_photo_unique_id,
                    "big_file_id": message.forward_from.photo.big_file_id,
                    "big_photo_unique_id": message.forward_from.photo.big_photo_unique_id,
                }
                if message.forward_from.photo
                else ""
            )

    elif message.from_user and message.from_user.photo:
        return {
            "small_file_id": message.from_user.photo.small_file_id,
            "small_photo_unique_id": message.from_user.photo.small_photo_unique_id,
            "big_file_id": message.from_user.photo.big_file_id,
            "big_photo_unique_id": message.from_user.photo.big_photo_unique_id,
        }
    elif (
        message.from_user
        or message.sender_chat
        and not message.sender_chat.photo
        or not message.sender_chat
    ):
        return ""
    else:
        return {
            "small_file_id": message.sender_chat.photo.small_file_id,
            "small_photo_unique_id": message.sender_chat.photo.small_photo_unique_id,
            "big_file_id": message.sender_chat.photo.big_file_id,
            "big_photo_unique_id": message.sender_chat.photo.big_photo_unique_id,
        }


async def get_text_or_caption(message: Message):
    if message.text:
        return message.text
    elif message.caption:
        return message.caption
    else:
        return ""


async def pyrogram_to_quotly(messages):
    if not isinstance(messages, list):
        messages = [messages]
    payload = {
        "type": "quote",
        "format": "png",
        "backgroundColor": "#ffffff",
        "messages": [],
    }

    for message in messages:
        the_message_dict_to_append = {}
        if message.entities:
            the_message_dict_to_append["entities"] = [
                {
                    "type": entity.type.name.lower(),
                    "offset": entity.offset,
                    "length": entity.length,
                }
                for entity in message.entities
            ]
        elif message.caption_entities:
            the_message_dict_to_append["entities"] = [
                {
                    "type": entity.type.name.lower(),
                    "offset": entity.offset,
                    "length": entity.length,
                }
                for entity in message.caption_entities
            ]
        else:
            the_message_dict_to_append["entities"] = []
        the_message_dict_to_append["chatId"] = await get_message_sender_id(message)
        the_message_dict_to_append["text"] = await get_text_or_caption(message)
        the_message_dict_to_append["avatar"] = True
        the_message_dict_to_append["from"] = {}
        the_message_dict_to_append["from"]["id"] = await get_message_sender_id(message)
        the_message_dict_to_append["from"]["name"] = await get_message_sender_name(
            message
        )
        the_message_dict_to_append["from"][
            "username"
        ] = await get_message_sender_username(message)
        the_message_dict_to_append["from"]["type"] = message.chat.type.name.lower()
        the_message_dict_to_append["from"]["photo"] = await get_message_sender_photo(
            message
        )
        if message.reply_to_message:
            the_message_dict_to_append["replyMessage"] = {
                "name": await get_message_sender_name(message.reply_to_message),
                "text": await get_text_or_caption(message.reply_to_message),
                "chatId": await get_message_sender_id(message.reply_to_message),
            }
        else:
            the_message_dict_to_append["replyMessage"] = {}
        payload["messages"].append(the_message_dict_to_append)
    r = await http.post("https://bot.lyo.su/quote/generate.png", json=payload)
    if not r.is_error:
        return r.read()
    else:
        raise QuotlyException(r.json())


def isArgInt(txt) -> list:
    count = txt
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]


@bots.on_message(filters.me & filters.command("q", cmd))
async def msg_quotly_cmd(client: Client, message):
    if len(message.text.split()) > 1:
        check_arg = isArgInt(message.command[1])
        if check_arg[0]:
            if check_arg[1] < 2 or check_arg[1] > 10:
                return await eor(
                    message, "<code>Argumen yang anda berikan salah...</code>", del_in=6
                )
            try:
                messages = [
                    i
                    for i in await client.get_messages(
                        chat_id=message.chat.id,
                        message_ids=range(
                            message.reply_to_message.id,
                            message.reply_to_message.id + (check_arg[1] + 5),
                        ),
                        replies=-1,
                    )
                    if not i.empty and not i.media
                ]
            except Exception as e:
                return await eor(message, f"<code>Error : {e}</code>")
            try:
                make_quotly = await pyrogram_to_quotly(messages)
                bio_sticker = BytesIO(make_quotly)
                bio_sticker.name = "biosticker.webp"
                return await message.reply_sticker(bio_sticker)
            except Exception as e:
                return await eor(message, f"<code>Error : {e}</code>")
    try:
        messages_one = await client.get_messages(
            chat_id=message.chat.id, message_ids=message.reply_to_message.id, replies=-1
        )
        messages = [messages_one]
    except Exception as e:
        return await eor(message, f"<code>Error : {e}</code>")
    try:
        make_quotly = await pyrogram_to_quotly(messages)
        bio_sticker = BytesIO(make_quotly)
        bio_sticker.name = "biosticker.webp"
        return await message.reply_sticker(bio_sticker)
    except Exception as e:
        return await eor(message, f"<code>Error : {e}</code>")


__MODULE__ = "quote"
__HELP__ = f"""
✘ Bantuan Untuk Quote

๏ Perintah: <code>{cmd}q</code> [balas pesan]
◉ Penjelasan: Untuk quote.

๏ Perintah: <code>{cmd}q</code> [balas pesan][angka]
◉ Penjelasan: Ini akan membuat beberapan pesan menjadi quote.
"""
