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

send_messages(messages[:], new_list)

print("\nFinal lists:")
print("Mesages", messages)
print("New list:", new_list)