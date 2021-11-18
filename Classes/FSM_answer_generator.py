from abc import ABC, abstractmethod

from Classes.message import Message
from settings import EmojiType
answers = {
    EmojiType.NONE: {
        EmojiType.NONE: 'Я тебя не понимаю',
        EmojiType.HAPPY: 'Привет добрый',
        EmojiType.SAD: 'Привет грустный',
        EmojiType.NEGATIVE: 'Привет злой'
    },
    EmojiType.HAPPY: {
        EmojiType.NONE: 'Я тебя не понимаю',
        EmojiType.HAPPY: 'Всё ещё добрый',
        EmojiType.SAD: 'Был добрый теперь грустный',
        EmojiType.NEGATIVE: 'Был добрый теперь злой'
    },
    EmojiType.SAD: {
        EmojiType.NONE: 'Я тебя не понимаю',
        EmojiType.HAPPY: 'Был грустный стал добрым',
        EmojiType.SAD: 'Всё ещё грустный',
        EmojiType.NEGATIVE: 'Был грустный стал злой'
    },
    EmojiType.NEGATIVE: {
        EmojiType.NONE: 'Я тебя не понимаю',
        EmojiType.HAPPY: 'Был злой стал добрый',
        EmojiType.SAD: 'Был злой стал грустный',
        EmojiType.NEGATIVE: 'Всё ещё злой'
    }
}


class AnswerGenerator(ABC):
    """
    Interface of Answer Generator
    """
    @abstractmethod
    def generate_answer(self, msg: Message, context: Message) -> str:
        """
        Should generate answer for given Message and context
        :return: Answer string
        """
        pass


class FSMGenerator(AnswerGenerator):
    """
    Implementation of AnswerGenerator on Final-State Machine method
    """
    def __init__(self):
        self.states = answers

    def generate_answer(self, msg: Message, context_message: Message) -> str:
        """
        Generates answer for given message and context. Uses Final-State Machine for processing
        :param msg: Input message
        :param context_message: Context message
        :return: answer
        """
        curr_type = msg.type
        if context_message:
            context_type = context_message.type
        else:
            context_type = EmojiType.NONE

        return self.states[context_type][curr_type]
