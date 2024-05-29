from interface.user_interface import UserInput


def main():
    # test_channels = [{"general": "CH172626"}, {"Sam": "CH1234"}]
    test_channels = {"general": "CH172626", "Sam": "CH1234"}
    print("Select any Channel/User to send a message to")
    channels = "\n".join([names for names in test_channels.keys()])
    print(channels)

    interface = UserInput()
    interface.get_channel_input()
    print(interface.channel_name)


if __name__ == "__main__":
    main()
