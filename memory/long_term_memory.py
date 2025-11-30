import json
import os

class LongTermMemory:
    FILE = "lifeflow_memory.json"

    def __init__(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.memory, f, indent=2)

    def write(self, key, value):
        self.memory[key] = value
        self.save()

    def read(self, key):
        return self.memory.get(key, None)
