from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="شخصي",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="عام", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ إغلاق ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="افضل 10 قوائم تشغيل", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="شخصي", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="عام", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="مجموعات", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="رجوع", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="إغلاق", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="الصوت", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="الفيديو", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="رجوع", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="إغلاق", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="افضل 10 قوائم تشغيل", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="شخصي", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="عام", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="مجموعات", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="رجوع", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="إغلاق", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="رجوع",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="إغلاق", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="حذف",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="رجوع",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="إغلاق",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ إغلاق ✯",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
