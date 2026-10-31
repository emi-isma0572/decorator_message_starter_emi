from messages.message import Message
from messages.plain_message import PlainMessage
from messages.timestamp_decorator import TimestampDecorator
from messages.urgent_decorator import UrgentDecorator


def main() -> None:
    plain = PlainMessage("Deploy complete")
    timestamp = "2026-10-30 14:30:00"

    message: Message = TimestampDecorator(UrgentDecorator(plain), timestamp)
    print(message.render())

    reversed_message: Message = UrgentDecorator(TimestampDecorator(plain, timestamp))
    print(reversed_message.render())


if __name__ == "__main__":
    main()
