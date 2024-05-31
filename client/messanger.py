from abc import ABC, abstractmethod
from .slack_client import SlackClient


class Messenger(ABC):
    @abstractmethod
    def get_receivers(self):
        pass

    @abstractmethod
    def get_receiver_names(self):
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

    def get_receiver_names(self):
        names = []
        for items in self.receivers:
            names.append(items.get("name"))

        return names

    def post_message(self, receiver: str, message: str):
        # Get receiver and check if channel or not to determine were to send message
        print(f"receiver: {receiver}")
        print(f"message: {message}")
        receiver_data = [
            data for data in self.receivers if data.get("name") == receiver
        ]
        if receiver_data:
            receiver_item = receiver_data[0]
        return receiver_data

    # def send_message(self, channel, message, record=None):
    #     """
    #     Send message to slack channel
    #     """
    #     slack = SlackClientAPI(self.slack_token, self, record)
    #     markdown = self.convert_html_to_markdown(message)
    #     response = slack.webclient_post_message(channel, markdown)
    #     return response

    # def user_direct_message(self, users: list, message, record=None):
    #     """
    #     Send a direct message to a user
    #     """
    #     slack = SlackClientAPI(self.slack_token, self, record)
    #     response = slack.webclient_open_conversation(users=users)
    #     if response:
    #         channel = response["channel"]["id"]
    #         markdown = self.convert_html_to_markdown(message)
    #         response = slack.webclient_post_message(channel, markdown)
    #     return response
