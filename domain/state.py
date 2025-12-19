class State():
    state = {}

    def __init__(self, initial_state=None):
        if initial_state:
            self.state.update(initial_state)

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key, None)
