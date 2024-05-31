from client.messanger import Messenger


class UserController:
    def __init__(self, messenger: Messenger, interface) -> None:
        self.messenger = messenger

        if not hasattr(interface, "receiver_name"):
            raise Exception("Object Does not have a receiver name")
        if not hasattr(interface, "message"):
            raise Exception("Object Does not have a message to send")
        else:
            self.interface = interface

    def send_message(self):
        return self.messenger.post_message(
            self.interface.receiver_name, self.interface.message
        )
