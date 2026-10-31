from .message import Message
from .message_decorator import MessageDecorator


class TimestampDecorator(MessageDecorator):
    """Prefix a supplied timestamp so rendering is deterministic."""

    def __init__(self, message: Message, timestamp: str):
        super().__init__(message)
        self._timestamp = timestamp

    def render(self) -> str:
        return f"[{self._timestamp}] {super().render()}"
