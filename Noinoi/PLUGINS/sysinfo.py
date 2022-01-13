# Copyright (C) 2021 Veez Project

import re
import uuid
import socket

import psutil
import platform
from Noinoi.config import BOT_USERNAME
from Noinoi.DREAMS.filters import command
from pyrogram import Client, filters
from Noinoi.DREAMS.decorators import sudo_users_only, humanbytes


# SYSTEM STATS

@Client.on_message(command(["gstats", f"gstats@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    somsg = f"""📊 **𝐒𝐘𝐒𝐓𝐄𝐌 𝐈𝐌𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 **
    
**𝚂𝚙𝚕𝚊𝚝𝚏𝚘𝚛𝚖 :** `{splatform}`
**𝙿𝚕𝚊𝚝𝚏𝚘𝚛𝚖 - Release :** `{platform_release}`
**𝙿𝚕𝚊𝚝𝚏𝚘𝚛𝚔 - Version :** `{platform_version}`
**𝙰𝚛𝚌𝚑𝚒𝚝𝚎𝚌𝚝𝚞𝚛𝚎 :** `{architecture}`
**𝙷𝚘𝚜𝚝𝚗𝚊𝚖𝚎 :** `{hostname}`
**𝙸𝙿 :** `{ip_address}`
**𝙼𝚊𝚌 :** `{mac_address}`
**𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚘𝚛 :** `{processor}`
**𝚁𝚊𝚖 : ** `{ram}`
**𝙲𝙿𝚄 :** `{cpu_len}`
**𝙲𝙿𝚄 𝙵𝚁𝙴𝚀 :** `{cpu_freq}`
**𝙳𝙸𝚂𝙺 :** `{disk}`
    """
    await message.reply(somsg)
