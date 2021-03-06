from enum import Enum

DB_NAME = 'emoji_bot.db'


class EmojiType(Enum):
    NONE = 0
    HAPPY = 1
    SAD = 2
    NEGATIVE = 3


EMOJIS = {
    '๐': EmojiType.HAPPY,
    '๐': EmojiType.HAPPY,
    '๐': EmojiType.HAPPY,
    '๐': EmojiType.HAPPY,
    '๐': EmojiType.HAPPY,
    '๐': EmojiType.HAPPY,
    '๐': EmojiType.HAPPY,
    '๐คฉ': EmojiType.HAPPY,
    '๐ฅณ': EmojiType.HAPPY,

    '๐': EmojiType.SAD,
    '๐': EmojiType.SAD,
    '๐': EmojiType.SAD,
    '๐': EmojiType.SAD,
    '๐': EmojiType.SAD,
    '๐': EmojiType.SAD,
    '๐ฉ': EmojiType.SAD,
    '๐ซ': EmojiType.SAD,
    '๐': EmojiType.SAD,

    '๐ฟ': EmojiType.NEGATIVE,
    '๐ฌ': EmojiType.NEGATIVE,
    '๐ค': EmojiType.NEGATIVE,
    '๐ก': EmojiType.NEGATIVE,
    '๐บ': EmojiType.NEGATIVE,
    '๐': EmojiType.NEGATIVE,
    '๐ ': EmojiType.NEGATIVE,
    '๐คฏ': EmojiType.NEGATIVE,
    '๐คจ': EmojiType.NEGATIVE
}

EMOJIS_TEST = {
    'happy': EmojiType.HAPPY,
    'happy1': EmojiType.HAPPY,
    'happy2': EmojiType.HAPPY,
    'happy3': EmojiType.HAPPY,
    'happy4': EmojiType.HAPPY,
    'happy5': EmojiType.HAPPY,
    'happy6': EmojiType.HAPPY,
    'happy7': EmojiType.HAPPY,
    'happy8': EmojiType.HAPPY,

    'sad': EmojiType.SAD,
    'sad1': EmojiType.SAD,
    'sad2': EmojiType.SAD,
    'sad3': EmojiType.SAD,
    'sad4': EmojiType.SAD,
    'sad5': EmojiType.SAD,
    'sad6': EmojiType.SAD,
    'sad7': EmojiType.SAD,
    'sad8': EmojiType.SAD,

    'neg': EmojiType.NEGATIVE,
    'neg1': EmojiType.NEGATIVE,
    'neg2': EmojiType.NEGATIVE,
    'neg3': EmojiType.NEGATIVE,
    'neg4': EmojiType.NEGATIVE,
    'neg5': EmojiType.NEGATIVE,
    'neg6': EmojiType.NEGATIVE,
    'neg7': EmojiType.NEGATIVE,
    'neg8': EmojiType.NEGATIVE
}
