import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

_logger = logging.getLogger(__name__)
from abc import ABC, abstractmethod


class SlackClient(ABC):

    @abstractmethod
    def users_list(self):
        pass

    @abstractmethod
    def conversation_list(self):
        pass

    @abstractmethod
    def conversation_open(self):
        pass

    @abstractmethod
    def chat_message(self):
        pass


class SlackWebClient(SlackClient):
    def __init__(self, token):
        self.client = WebClient(token=token)

    def users_list(self):
        try:
            response = self.client.users_list()
            return response
        except SlackApiError as e:
            _logger.error(f"Error getting users list: {e}")

            return False

    def conversation_list(self):
        try:
            channel_types = "public_channel, private_channel"
            response = self.client.conversations_list(types=channel_types)
            return response
        except SlackApiError as e:
            _logger.error(f"Error getting conversations list: {e}")

            return False

    def conversation_open(self):
        pass

    def chat_message(self):
        pass

    # def webclient_post_message(self, channel: str, message: str):
    #     try:
    #         response = self.web_client.chat_postMessage(channel=channel, text=message)
    #         return response
    #     except SlackApiError as e:
    #         _logger.info(f"Error sending message to channel {channel}: {e}")
    #         if self.record:
    #             self.record.ihub_error(e)
    #         return e

    # def webclient_open_conversation(self, users: list, return_im=True):
    #     """Open a conversation with a user."""

    #     try:
    #         response = self.web_client.conversations_open(
    #             return_im=return_im, users=users
    #         )
    #         return response
    #     except SlackApiError as e:
    #         _logger.info(f"Error opening conversation with users {users}: {e}")
    #         if self.record:
    #             self.record.ihub_error(e)
    #         return e
