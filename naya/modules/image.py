# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

import asyncio
import os

import cv2
from pyrogram import *
from pyrogram.types import *

from . import *


@bots.on_message(filters.me & filters.command(["face"], cmd))
async def face_detect(c: Client, m: Message):
    pro = await eor(message, "`Processing...`")
    await asyncio.sleep(5)
    if not m.reply_to_message or not m.reply_to_message.photo:
        await pro.edit("Mohon balas ke foto wajah.")
        return

    file_id = m.reply_to_message.photo.file_id
    file_path = await c.download_media(file_id)
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite("naya/resources/output.jpg", img)
    await pro.edit("`Processing Upload`")
    await m.reply_photo(
        "naya/resources/output.jpg", caption="**Inilah wajah yang terdeteksi.**"
    )
    try:
        cleared = "naya/resources/output.jpg"
        os.remove(cleared)
    except BaseException:
        pass


@bots.on_message(filters.me & filters.command(["sketch", "pcil"], cmd))
async def generate_sketch(c: Client, m: Message):
    if m.reply_to_message.photo:
        file_id = m.reply_to_message.photo
        photo_path = await c.download_media(file_id)

        img = cv2.imread(photo_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted_img = 255 - gray_img
        blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)
        pencil_sketch = cv2.divide(gray_img, blurred_img, scale=80)
        sketch_path = "naya/resources/pencil_sketch.jpg"
        cv2.imwrite(sketch_path, pencil_sketch)

        await m.reply_photo(photo=sketch_path, caption=f"**Create by {c.me.mention}**")
        os.remove(photo_path)
        os.remove(sketch_path)


__MODULE__ = "Image"
__HELP__ = f"""
๏ Perintah: <code>{cmd}pcil or sketch</code>
◉ Penjelasan: Membuat gambar hitam putih.

๏ Perintah: <code>{cmd}face</code>
◉ Penjelasan: Mendeteksi wajah pada gambar. 
"""
