from interface.user_interface import UserInput
from interface.user_controller import UserController
from client.messanger import Slack
from client.slack_client import SlackWebClient


def main():
    # test_channels = [{"general": "CH172626"}, {"Sam": "CH1234"}]
    # test_channels = {"general": "CH172626", "Sam": "CH1234"}
    # print("Select any Channel/User to send a message to")
    # channels = "\n".join([names for names in test_channels.keys()])
    # print(channels)

    slack = Slack(
        SlackWebClient(
            token="xoxb-7199507593073-7184201220389-cOETYJUglSyr7DGe1WP43NK5"
        )
    )
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
