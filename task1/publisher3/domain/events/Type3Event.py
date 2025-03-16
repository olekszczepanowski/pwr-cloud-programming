import json


class Type3Event:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return f"Event({self.name}, {self.message})"

    def serialize(self):
        return json.dumps({"name": self.name, "data": self.message})

    @staticmethod
    def deserialize(body):
        decoded = json.loads(body)
        return Type3Event(decoded["name"], decoded["data"])
