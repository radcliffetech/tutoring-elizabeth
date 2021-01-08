message = {
    'to_name': to_name,
    'to_address': to_address,
    'from_name': from_name,
    'from_address': from_address,
    'subject': "Quantum building suggestions",
    'message_body': "Heya Al, what you do you think about relavitivy and structural strength? Love ya, Bob",
}

message2 = {
    'to_name': to_name,
    'to_address': to_address,
    'from_name': from_name,
    'from_address': from_address,
    'subject': "hey man",
    'message_body': "haven't heard from you what is going on",
}

class Mailbox():

    def __init__(self):
        """constructor - instantiates the object with its own parameters"""
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def contents(self):
        print("There are " + str(len(self.messages)) + " in this mailbox")


mailbox = Mailbox()
mailbox2 = Mailbox()

mailbox.add(message)
mailbox2.add(message2)


mailbox.contents()
mailbox2.contents()
