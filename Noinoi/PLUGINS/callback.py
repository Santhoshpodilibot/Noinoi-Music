# Β© NOINOI MUSIC @CFC_BOT_SUPPORT

from Noinoi.DREAMS.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Noinoi.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π­ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

π‘ **Find out all the Bot's commands and how they work by clicking on the Β» π Commands button!**

π **To know how to use this bot, please click on the Β» β Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("π’ π‘ππ§ πͺπ’π₯π", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("κ±α΄α΄Κα΄α΄", url="https://T.ME/newsstreamer"),
                InlineKeyboardButton("β¨ κ±α΄α΄α΄α΄Κα΄", url=f"https://t.me/{UPDATES_CHANNEL}"),],
                [InlineKeyboardButton("π π¦ππ‘π§ππ¨ ππ’π π ππ‘ππ¦", callback_data="cbcmds"),
                InlineKeyboardButton("β π¦ππ‘π§ππ¨ ππππ£", callback_data="cbsetup"),],
                [InlineKeyboardButton(" π½πππ πππ πππππ kondiπ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **Basic Guide for using this bot:**
        


1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

π **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

π‘ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ π¦ππ‘π§ππ¨ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Κ α΄ α΄ α΄", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Β» **press the button below to read the explanation and see the list of available commands !**

**β¨ α΄α΄α΄‘α΄Κα΄ Κπ ππ?π»ππ΅π α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π·π» α΄α΄α΄ΙͺΙ΄ α΄α΄α΄", callback_data="cbadmin"),
                    InlineKeyboardButton("π§π» κ±α΄α΄α΄ α΄α΄α΄", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("π Κα΄κ±Ιͺα΄ α΄α΄α΄", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("Κ α΄ α΄ α΄", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? here is the basic commands:

β― /play (song name/link) - play music on video chat
β― /playlist - show you the playlist
β― /lyric (query) - scrap the song lyric
β― /search (query) - search a youtube video link
β― /ping - show the bot ping status
β― /uptime - show the bot uptime status
β― /alive - show the bot alive info (in group)

 **β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? here is the admin commands:

β― /pause - pause the stream
β― /resume - resume the stream
β― /skip - switch to next stream
β― /stop - stop the streaming
β― /vmute - mute the userbot on voice chat
β― /vunmute - unmute the userbot on voice chat
β― /volume `1-200` - adjust the volume of music (userbot must be admin)
β― /reload - reload bot and refresh the admin data
β― /userbotjoin - invite the userbot to join group
β― /userbotleave - order userbot to leave from group

**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? here is the sudo commands:

β― /rmw - clean all raw files
β― /rmd - clean all downloaded files
β― /sysinfo - show the system information
β― /update - update your bot to latest version
β― /restart - restart your bot
β― /leaveall - order userbot to leave from all group

**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nΒ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"βοΈ **settings of** {query.message.chat.title}\n\nβΈ : pause stream\nβΆοΈ : resume stream\nπ : mute userbot\nπ : unmute userbot\nβΉ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("βΉ", callback_data="cbstop"),
                      InlineKeyboardButton("βΈ", callback_data="cbpause"),
                      InlineKeyboardButton("βΆοΈ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("π", callback_data="cbmute"),
                      InlineKeyboardButton("π", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("π Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)

# SETUP BUTTON OPEN......................................................................................................................................................................................

@Client.on_callback_query(filters.regex("cbsetup"))
async def cbsetup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello !**
Β» **press the button below to read the explanation and see the help commands !**
**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("welcome", callback_data="noiwel"),
                    InlineKeyboardButton("Lyric", callback_data="noilyric"),
                    InlineKeyboardButton("voice", callback_data="noivoice"),
                ],
                [
                    InlineKeyboardButton("How To Add Me β", callback_data="cbhowtouse"),
                ],
                [InlineKeyboardButton("π Go Back", callback_data="cbstart")],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noiwel"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **HEAR THE WELCOME PLUGIN ( soon )**

β― /setwelcome for set welcome message.

β― /resetwelcome for reset welcome message.

**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbsetup")]]
        ),
    )
@Client.on_callback_query(filters.regex("noilyric"))
async def noilyric(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **HEAR THE LYRIC PLUGIN**

β― /lyric ( song name ) for the get lyric of song

**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbsetup")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("noivoice"))
async def noivoice(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **HEAR THE VOICE PLUGIN**

β― /tts fot get voice from text message

**β¨ α΄α΄α΄‘α΄Κα΄ ΚΚ Ι΄α΄ΙͺΙ΄α΄Ιͺ α΄α΄κ±Ιͺα΄** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbsetup")]]
        ),
    )    

    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
