class BaseComponent:

    def __init__(self, root, state):
        self.root = root
        self.state = state
        self.components = {}

    def registerComponent(self, name, component):
        self.components[name] = component

    def setup(self):
        return None

    def pack(self):
        self.setup()
        self.root.pack()

        for name, childComponent in self.components.items():
            print(f"Adding child component: {name} -> {childComponent}")
            childComponent.pack()