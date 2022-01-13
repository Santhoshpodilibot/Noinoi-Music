import io
from os import path
from typing import Callable
from asyncio.queues import QueueEmpty
import os
import random
import aiofiles
import aiohttp
import converter
import ffmpeg
import requests
from PIL import Image, ImageDraw, ImageFont

FOREGROUND_IMG = [
    "Noinoi/IMAGES/LightBlue.png",
    "Noinoi/IMAGES/Orange.png",
    "Noinoi/IMAGES/Red.png",
    "Noinoi/IMAGES/Violate.png",
    "Noinoi/IMAGES/Grey.png",
]

aiohttpsession = aiohttp.ClientSession()
chat_id = None
useer = "NaN"
DISABLED_GROUPS = []

def cb_admin_check(func: Callable) -> Callable:
    async def decorator(client, cb):
        admemes = a.get(cb.message.chat.id)
        if cb.from_user.id in admemes:
            return await func(client, cb)
        else:
            await cb.answer("💡 only admin can tap this button !", show_alert=True)
            return

    return decorator


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", 
        format="s16le", 
        acodec="pcm_s16le", 
        ac=2, 
        ar="48k"
    ).overwrite_output().run()
    os.remove(filename)

def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def thumb(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"Noinoi/OTHERS/search/thumb{userid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(f"Noinoi/OTHERS/search/thumb{userid}.png")
    FOREGROUND_THUMBNAIL = random.choice(FOREGROUND_IMG)
    image2 = Image.open(FOREGROUND_THUMBNAIL)
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"Noinoi/OTHERS/search/temp{userid}.png")
    img = Image.open(f"Noinoi/OTHERS/search/temp{userid}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Noinoi/IMAGES/regular.ttf", 52)
    font2 = ImageFont.truetype("Noinoi/IMAGES/medium.ttf", 76)
    draw.text(
        (25, 610),
        f"{title[:18]}...",
        fill="black",
        font=font2,
    )
    draw.text(
        (27, 535),
        f"Playing on {ctitle[:8]}...",
        fill="black",
        font=font,
    )
    img.save(f"Noinoi/OTHERS/search/final{userid}.png")
    os.remove(f"Noinoi/OTHERS/search/temp{userid}.png")
    os.remove(f"Noinoi/OTHERS/search/thumb{userid}.png")
    final = f"Noinoi/OTHERS/search/final{userid}.png"
    return final
