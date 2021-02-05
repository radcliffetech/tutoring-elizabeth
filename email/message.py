to_name = "Albert Einstein"
to_address = "albert@example.com"
from_name = "Bob the Builder"
from_address = "bobbybuildz@example.com"

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


"""
CLASS

INSTANCE - a single instance of a class
"""

class Mailbox():

    def __init__(self, name, address):
        """constructor - instantiates the object with its own parameters"""
        self.messages = []
        self.name = name
        self.address = address

    def add(self, message):
        self.messages.append(message)

    def contents(self):
        print("There are " + str(len(self.messages)) + " messages in " + str(self))

    def get_mail(self):
        """empty mailbox and return messages"""
        messages = self.messages
        self.messages = []
        return messages

    def __str__(self):
        return "Mailbox " + self.name


class Mailperson():

    def __init__(self, name, mail_route):
        self.bag = []
        self.name = name
        self.mail_route = mail_route

    def say_hello(self):
        print("Hi, name name is " + self.name + ". I deliver mail! My route is " + str(len(self.mail_route)) + " boxes")

    def show_bag_status(self):
        print("I have " + str(len(self.bag)) + " things in my mailbag!")

    def collect_mail(self, mailbox):
        for mail_item in mailbox.get_mail():
            self.bag.append(mail_item)

    def deliver_mail(self):

        for mailbox in self.mail_route:
            for mail_item in self.bag:
                print(f"{mail_item['to_address']} <=> {mailbox.address}")
                if mail_item['to_address'] == mailbox.address:
                    mailbox.add(mail_item)  # this is for this mailbox!!


mailbox = Mailbox(name="Albert's Mailbox", address='albert@example.com')
mailbox_bob = Mailbox(name="Bob's Mailbox", address='bobbybuildz@example.com')
mailbox_annie = Mailbox(name="Annie's Mailbox", address='anniebananie@example.com')


fred = Mailperson(name='Fred', mail_route=[mailbox, mailbox_bob, mailbox_annie])
fred.say_hello()

mailbox.add(message)
mailbox.add(message2)

assert len(mailbox.messages) == 2

fred.collect_mail(mailbox)
assert len(fred.bag) == 2
assert len(mailbox.messages) == 0

# pick up mail
fred.show_bag_status()

# route mail
fred.deliver_mail()
assert len(mailbox_bob.messages) == 0
assert len(mailbox_annie.messages) == 0
assert len(mailbox.messages) == 2
assert len(fred.bag) == 0
