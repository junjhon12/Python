def show_messages(message):
    for messages in message:
        print(messages)
"""
def send_messages(message):
    while message:
        msg = f"{messages}"
        print(msg)
        old_list = messages.pop()
        new_list.append(old_list)
    for j in new_list:
        print(j)
"""

# Corrected code
def send_messages(message, new_list):
    while messages:
        msg = messages.pop()
        print(f"Sending message: {msg}")
        new_list.append(msg)
        
        
messages = [
    'message1',
    'message2',
    'message3'
]

new_list = []

show_messages(messages)
print()
send_messages(messages, new_list)

print("\nFinal lists:")
print("Messages:", messages)
print("Sent messages:", new_list)