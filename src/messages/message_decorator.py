from .message import Message


class MessageDecorator(Message):
    """Wrap a Message while preserving its render contract."""

    def __init__(self, message: Message):
        self._message = message

    def render(self) -> str:
        return self._message.render()
