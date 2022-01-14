from datetime import datetime
from sys import version_info
from time import time

from Noinoi.config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Noinoi.PLUGINS import version
from Noinoi.DREAMS.cfc import user
from Noinoi.DREAMS.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import version as pyrover
from pytgcalls import (version as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

major = 0
minor = 2
micro = 1

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ ʜᴇʟʟᴏ ɪ ᴀᴍ {message.from_user.mention()} !\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) !

💡 **ɴᴀɴᴜ ᴏᴋᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ʙᴏᴛ 
ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠɪᴅᴇᴏ sᴜᴘᴘᴏʀᴛ
ᴀ ᴄᴀᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ

ᴘᴏᴡᴇʀᴇᴅ ʙʏ ⚡(https://t.me/Santhoshpodilivcplayer1234bot) **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ꜱᴏᴜʀᴄᴇ", url="https://t.me/Catmusicworld"),
                InlineKeyboardButton("✨ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{UPDATES_CHANNEL}"),],
                [InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="cbcmds"),
                InlineKeyboardButton("❓ ꜱᴇᴛᴜᴘ", callback_data="cbsetup"),],
                [InlineKeyboardButton(" ᴀᴅᴅ ᴍᴇᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"Hello {message.from_user.mention()}, i'm {BOT_NAME}\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: v{version}\n🍀 Pyrogram Version: {pyrover}\n✨ Python Version: {python_version}\n🍀 PyTgCalls version: {pytover.version}\n✨ Uptime Status: {uptime}\n\nThanks for Adding me here, for playing video & music on your Group's video chat ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 PONG!!\n" f"⚡️ {delta_ping * 1000:.3f} ms")
