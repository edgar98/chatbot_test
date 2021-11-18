

class MessageProcessor:
    """
    Class for user message processing
    """
    def __init__(self, alphabet, generator):
        """
        Creates instance of Message class
        :param alphabet: Dictionary of possible input
        :type alphabet: dict
        :param generator: AnswerGenerator instance
        :type generator: Classes.FSM_answer_generator.AnswerGenerator
        """
        self.alphabet = alphabet
        self.generator = generator
        self.message = None
        self.context = None

    def process(self, message, context_msg) -> (str, bool):
        """
        Generates answer for given message, depended on context
        :param message: Message to answer
        :type message: Classes.message.Message
        :param context_msg: Context message
        :type context_msg: Classes.message.Message
        :return: Answer and error if message not in possible input dict
        """
        self.message = message
        self.context = context_msg
        error = self._check_message()
        return self._generate_answer(), error

    def _check_message(self) -> bool:
        """
        Checks message in input dict
        """
        if self.message.text in self.alphabet:
            self.message.set_type(self.alphabet[self.message.text])
            return False
        else:
            return True

    def _generate_answer(self) -> str:
        """
        Generates answer using answer generator
        :return:
        """
        return self.generator.generate_answer(self.message, self.context)
