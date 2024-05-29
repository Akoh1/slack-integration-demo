class UserInput:
    def __init__(self) -> None:
        self.channel_name = None
        self.message = None

    def get_channel_input(self):
        self.channel_name = input(
            "Enter Channel(s) name(for more than 1 channel/user separate by space): "
        )

    def get_message_input(self):
        self.message = input("Enter message to send: ")
