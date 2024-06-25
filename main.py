import os
from dotenv import load_dotenv
from interface.user_interface import UserInput
from interface.user_controller import UserController
from client.messanger import Slack
from client.slack_client import SlackWebClient


def main():

    load_dotenv()

    print(f"token: {os.getenv('token')}")

    slack = Slack(SlackWebClient(token=os.getenv("token")))
    print(slack.get_receivers())
    channels = slack.get_receiver_names()
    channels = "\n".join([name for name in channels])
    print("Select any Channel/User to send a message to")
    print(channels)

    interface = UserInput()
    interface.get_channel_input()
    print(interface.receiver_name)
    interface.get_message_input()
    print(interface.message)

    controller = UserController(slack, interface)
    print(controller.send_message())


if __name__ == "__main__":
    main()
