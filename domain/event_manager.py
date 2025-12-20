
class EventManager:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, key, callback):
            if not hasattr(self, '_subscribers'):
                self._subscribers = {}
            if key not in self._subscribers:
                self._subscribers[key] = []
            self._subscribers[key].append(callback)

    def _notify_subscribers(self, key):
        if hasattr(self, '_subscribers') and key in self._subscribers:
            for callback in self._subscribers[key]:
                callback("")