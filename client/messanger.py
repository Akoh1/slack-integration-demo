from abc import ABC, abstractmethod
from .slack_client import SlackClient


class Messenger(ABC):
    """Interface for other message types to implement"""

    @abstractmethod
    def get_receivers(self):
        """Get list of receivers Data"""
        pass

    @abstractmethod
    def get_receiver_names(self) -> list:
        """Get List of receivers name"""
        pass

    @abstractmethod
    def post_message(self, receiver, message):
        pass


class Slack(Messenger):
    def __init__(self, client: SlackClient) -> None:
        self.client = client
        self.receivers = None

    def get_receivers(self):
        channels_list = self.client.conversation_list()
        users_list = self.client.users_list()
        receivers = []
        if channels_list:
            receivers = channels_list.get("channels")
        if users_list:
            receivers += [
                member for member in users_list["members"] if member["is_bot"] is False
            ]

        self.receivers = receivers

    def get_receiver_names(self) -> list:
        names = []
        for items in self.receivers:
            names.append(items.get("name"))

        return names

    def post_message(self, receiver: str, message: str):
        # Get receiver and check if channel or not to determine were to send message

        receiver_data = [
            data for data in self.receivers if data.get("name") == receiver
        ]
        if receiver_data:
            receiver_item = receiver_data[0]
            if receiver_item.get("is_channel") is True:
                channel = receiver_item.get("id")
                self.client.chat_message(channel, message)
            else:
                print(f"rec id: {receiver_item.get('id')}")
                receiver_id = receiver_item.get("id").split()
                response = self.client.conversation_open(receivers=receiver_id)
                if response:
                    channel = response["channel"]["id"]
                    self.client.chat_message(channel, message)
        return True
