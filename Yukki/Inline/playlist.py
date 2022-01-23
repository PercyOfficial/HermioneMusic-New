from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ 🇮",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ📽️",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ🥳",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"ʀᴀᴘ⚡",
                callback_data=f"play_playlist {user_id}|{type}|Rap",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʙᴛs💜",
                callback_data=f"play_playlist {user_id}|{type}|Bts",
            ),
            InlineKeyboardButton(
                text=f"sɪɴʜᴀʟᴀ🇱🇰",
                callback_data=f"play_playlist {user_id}|{type}|Sinhala",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴅᴊ-ʀᴇᴍɪx💃",
                callback_data=f"play_playlist {user_id}|{type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"ᴏᴛʜᴇʀ🤔",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"sɪɴʜᴀʟᴀ🇱🇰",
                callback_data=f"add_playlist {videoid}|{type}|Sinhala",
            ),
            InlineKeyboardButton(
                text=f"ʙᴛs💜",
                callback_data=f"add_playlist {videoid}|{type}|Bts",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ🥳",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"ʀᴀᴘ⚡",
                callback_data=f"add_playlist {videoid}|{type}|Rap",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ 🇮🇪",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ📽️",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴅᴊ-ʀᴇᴍɪx💃",
                callback_data=f"add_playlist {videoid}|{type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"ᴏᴛʜᴇʀ🤔",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"sɪɴʜᴀʟᴀ🇱🇰", callback_data=f"check_playlist {type}|Sinhala"
            ),
            InlineKeyboardButton(
                text=f"ʙᴛs💜", callback_data=f"check_playlist {type}|BTS"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ🥳", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"ʀᴀᴘ⚡", callback_data=f"check_playlist {type}|Rap"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ 🇮",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ📽️",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴅᴊ-ʀᴇᴍɪx💃",
                callback_data=f"check_playlist {type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"ᴏᴛʜᴇʀ🤔", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
