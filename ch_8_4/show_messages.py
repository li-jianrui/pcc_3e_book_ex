def show_messages(messages):
    """Print each message in the list of messages."""
    for message in messages:
        print(message)

messages = ['Hello, world!', 'Python is awesome!', 'Functions are great!']
show_messages(messages)

sent_messages = []

def send_messages(messages, sent_messages):
    """Simulate sending each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)