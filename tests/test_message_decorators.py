from messages.message import Message
from messages.plain_message import PlainMessage
from messages.timestamp_decorator import TimestampDecorator
from messages.urgent_decorator import UrgentDecorator


def test_stacked_decorators_preserve_contract_and_show_order():
    plain = PlainMessage("Deploy complete")
    timestamp = "2026-10-30 14:30:00"

    timestamp_outside = TimestampDecorator(UrgentDecorator(plain), timestamp)
    urgent_outside = UrgentDecorator(TimestampDecorator(plain, timestamp))

    assert isinstance(timestamp_outside, Message)
    assert isinstance(urgent_outside, Message)
    assert timestamp_outside.render() == "[2026-10-30 14:30:00] [URGENT] Deploy complete"
    assert urgent_outside.render() == "[URGENT] [2026-10-30 14:30:00] Deploy complete"
    assert plain.render() == "Deploy complete"
