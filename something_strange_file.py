import torch


class ErrorDetectionModel(torch.nn.Module):
    """
        Detection and clacivier error
    """
    def __init__(self) -> None:
        """init the model for detection erors"""
        super(ErrorDetectionModel, self).__init__()
        pass

    def forward(self, x) -> None:
        """calculate"""
        pass

    def save(self, path, overwrite = True, **kwargs) -> None:
        pass

    def load(self, path_or_state, overwrite_lr = True, strict = True) -> None:
        pass


class RecomendSystem():
    def __init__(self) -> None:
        """init the model for detection erors"""
        pass

    def forward(self, x) -> None:
        """calculate"""
        pass

    def save(self, path, overwrite = True, **kwargs) -> None:
        pass

    def load(self, path_or_state, overwrite_lr = True, strict = True) -> None:
        pass



class ChatBot():
    """
        A conversational dialog chat bot.
    """
    def __init__(self, name, **kwargs) -> None:
        pass

    def get_response(self, statement=None, **kwargs):
        """
        Return the bot's response based on the input.
        :param statement: An statement object or string.
        :returns: A response to the input.
        :rtype: Statement
        :param additional_response_selection_parameters: Parameters to pass to the
            chat bot's logic adapters to control response selection.
        :type additional_response_selection_parameters: dict
        :param persist_values_to_response: Values that should be saved to the response
            that the chat bot generates.
        :type persist_values_to_response: dict
        """
        pass

    def generate_response(self, input_statement, additional_response_selection_parameters=None):
        """
        Return a response based on a given input statement.
        :param input_statement: The input statement to be processed.
        """
        pass

    def learn_response(self, statement, previous_statement=None):
        """
        Learn that the statement provided is a valid response.
        """
        pass
