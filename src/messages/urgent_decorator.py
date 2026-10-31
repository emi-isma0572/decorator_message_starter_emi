from .message_decorator import MessageDecorator


class UrgentDecorator(MessageDecorator):
    """Mark the wrapped message as urgent."""

    def render(self) -> str:
        return f"[URGENT] {super().render()}"
