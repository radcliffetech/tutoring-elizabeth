class Backpack:

    def __init__(self, name):
        self.name = name
        self.items = []

    def look_items(self):
        for item in self.items:
            print("found a " + item)

    def add_item(self, item):
        self.items.append(item)
