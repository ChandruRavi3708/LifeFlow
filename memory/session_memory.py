class SessionMemory:
    def __init__(self):
        self.state = {}

    def write(self, key, value):
        self.state[key] = value

    def read(self, key):
        return self.state.get(key)
