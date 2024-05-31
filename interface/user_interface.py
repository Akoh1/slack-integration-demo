class UserInput:
    def __init__(self) -> None:
        self.receiver_name = None
        self.message = None

    def get_channel_input(self):
        self.receiver_name = input("Enter Receiver Name: ")

    def get_message_input(self):
        self.message = input("Enter message to send: ")
